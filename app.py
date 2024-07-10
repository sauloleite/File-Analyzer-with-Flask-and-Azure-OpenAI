import os
import base64
import requests
from openai import AzureOpenAI
from flask import Flask, redirect, render_template, request, send_from_directory, url_for, abort
from docx import Document
from unidecode import unidecode
import fitz  # PyMuPDF
from pptx import Presentation

# Configuração da API da OpenAI
client = AzureOpenAI(
    azure_endpoint="insira_aqui_o_endpoint_da_sua_chave_azure",
    api_key='insira_aqui_a_sua_chave_azure',
    api_version="insira_aqui_a_versao_da_api" #"2024-02-01"
)

# Função para extrair texto e imagens de arquivos DOCX
def extractContentDocs(arquivo):
    documento = Document(arquivo)
    content = []
    for para in documento.paragraphs:
        content.append(para.text)  # Adiciona o texto de cada parágrafo ao conteúdo
    
    for rel in documento.part.rels.values():
        if "image" in rel.target_ref:
            image = rel.target_part.blob  # Adiciona as imagens ao conteúdo
            content.append(image)
    
    return content

# Função para extrair texto e imagens de arquivos PDF
def extractContentPdf(arquivo):
    documento = fitz.open(stream=arquivo.read(), filetype="pdf")
    content = []
    for pagina in documento:
        text = pagina.get_text()  # Adiciona o texto de cada página ao conteúdo
        content.append(text)
        for img in pagina.get_images(full=True):
            xref = img[0]
            base_image = documento.extract_image(xref)
            image_bytes = base_image["image"]  # Adiciona as imagens ao conteúdo
            content.append(image_bytes)
    return content

# Função para extrair texto e imagens de arquivos PPT/PPTX
def extractContentPpt(arquivo):
    prs = Presentation(arquivo)
    content = []
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text = shape.text  # Adiciona o texto de cada slide ao conteúdo
                content.append(text)
            elif hasattr(shape, "image"):
                image = shape.image.blob  # Adiciona as imagens ao conteúdo
                content.append(image)
    return content

# Função para enviar imagem para ImgBB e obter a URL pública
def upload_image_to_imgbb(image_bytes):
    imgbb_api_key = 'insira_aqui_a_sua_chave_imgbb'
    imgbb_url = 'https://api.imgbb.com/1/upload'
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    payload = {
        'key': imgbb_api_key,
        'image': image_base64
    }
    imgbb_response = requests.post(imgbb_url, data=payload)
    if imgbb_response.status_code == 200:
        imgbb_data = imgbb_response.json()
        public_image_url = imgbb_data['data']['url']  # URL pública da imagem
        delete_url = imgbb_data['data']['delete_url']  # URL para deletar a imagem
        return public_image_url, delete_url
    return None, None

# Função para descrever imagem usando OpenAI
def describe_image(image_url):
    response = client.chat.completions.create(
        model="insira_aqui_o_modelo_da_openai",
        messages=[
            { "role": "system", "content": "Você é um excelente assistente para descrever imagens." },
            { "role": "user", "content": [  
                { 
                    "type": "text", 
                    "text": "Descreva esta imagem:" 
                },
                { 
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ] } 
        ],
    )
    return response.choices[0].message.content  # Retorna a descrição da imagem

# Função para extrair e converter texto de arquivos TXT
def extractTextTxts(arquivo):
    try:
        texto = arquivo.read().decode("utf-8")
        return unidecode(texto)  # Remove acentuações do texto
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado.")
        return None

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota para a página principal
@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

# Rota para o favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Rota para processar o resultado da submissão do formulário
@app.route('/result', methods=['POST'])
def result():
    try:
        file = request.files.get('file')
        if file and file.filename != '':
            print('Request for result page received with file')
            ext = os.path.splitext(file.filename)[1].lower()
            content = []
            image_base64 = None

            # Extrai conteúdo baseado na extensão do arquivo
            if ext == '.docx':
                content = extractContentDocs(file)
            elif ext == '.pdf':
                content = extractContentPdf(file)
            elif ext == '.txt':
                content.append(extractTextTxts(file))
            elif ext == '.pptx':
                content = extractContentPpt(file)
            elif ext in ['.png', '.jpeg', '.jpg']:
                image_bytes = file.read()
                image_base64 = base64.b64encode(image_bytes).decode('utf-8') # Codifica a imagem em base64
                public_image_url, delete_url = upload_image_to_imgbb(image_bytes)
                if public_image_url:
                    descricao = describe_image(public_image_url)
                    content.append(descricao)
                    requests.get(delete_url) 

            final_content = ""
            # Concatena o conteúdo extraído em uma string final
            for item in content:
                if isinstance(item, str):
                    final_content += item + "\n"
                elif isinstance(item, bytes):
                    public_image_url, delete_url = upload_image_to_imgbb(item)
                    if public_image_url:
                        descricao = describe_image(public_image_url)
                        final_content += descricao + "\n"
                        requests.get(delete_url) 

            # Extrai o prompt do arquivo "prompts.txt" para a OpenAI
            prompt = extractTextTxts(open('prompts.txt', 'rb'))
            response = client.chat.completions.create(
                model="insira_aqui_o_modelo_da_openai",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": final_content}
                ],
                max_tokens=1000 # Limite de tokens para a resposta
            )
            content = response.choices[0].message.content
            content = content.replace('**', '') # Remove os marcadores de negrito
            
            with open("output.txt", 'w', encoding='utf-8') as arquivo:
                arquivo.write(content)
            return render_template('result.html', txt=content, image_base64=image_base64)
            
        print('Request for result page received with no file or unsupported file type -- redirecting')
        return redirect(url_for('index'))

    except Exception as e:
        # Log the exception
        print(f"Erro: {e}")
        # Renderiza a página result.html com a mensagem de erro
        return render_template('result.html', txt="Ops... tivemos um problema e não foi possível analisar o documento. Por favor, tente novamente mais tarde", image_base64=None)

# Manipulador de erro para exceções não tratadas
@app.errorhandler(Exception)
def handle_exception(e):
    # Você pode adicionar logging aqui se quiser
    print(f"Erro: {e}")
    # Renderiza a página result.html com a mensagem de erro
    return render_template('result.html', txt="Ops... tivemos um problema e não foi possível analisar o documento. Por favor, tente novamente mais tarde", image_base64=None)

if __name__ == '__main__':
    app.run()

#Antes de realizar os ajustes do seu código: realize o comando: pip install -r requirements.txt
#Insira no código as chaves da OpenAI e da ImgBB e o endpoint da sua chave Azure
#Para executar a aplicação, execute o seguinte comando no terminal: flask run
#Ao execultar a aplicação pela primeira vez é solicitada uma autenticação que é login:admin e senha:admin321
#Qualquer dúvida, mande um email para sjoldeveloper@gmail.com
