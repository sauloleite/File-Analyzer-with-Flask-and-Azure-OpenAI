# Analisador de Arquivos com Flask e Azure OpenAI

Esta aplicação é um WebApp que permite aos usuários enviar arquivos para criação de resumos, análises e descrições utilizando os serviços da Azure, incluindo a API Azure OpenAI.

## Arquitetura

### Partes da Arquitetura

1. **Usuários:**
   - Enviam arquivos através do navegador (Browser).

2. **Recurso em Azure:**
   - **Resource Group:** Agrupamento dos serviços utilizados na arquitetura.
   - **App Service Plan:** Fornece a base para o funcionamento do aplicativo, disponibilizando os recursos subjacentes necessários.
   - **App Service Web App:** Hospeda o aplicativo Web Python em um ambiente de servidor Linux.

3. **Tecnologias Utilizadas:**
   - HTML, CSS, JS, Bootstrap: Tecnologias para criar e estilizar a interface do usuário.
   - Python: Linguagem para desenvolver a lógica do aplicativo.
   - Flask: Framework usado para estruturar o aplicativo Web e fornecer os recursos básicos.
   - API Azure OpenAI: Processa os textos extraídos utilizando o modelo de linguagem GPT-4o para gerar resumos, análises e descrições.

### Passo a Passo do Funcionamento

1. Usuários enviam arquivos através do navegador.
2. O App Service Plan oferece infraestrutura de suporte ao WebApp.
3. O WebApp, hospedado no App Service Web App, utiliza Flask para gerenciar a aplicação em Python.
4. A interface do aplicativo é desenvolvida com HTML, CSS, JS e Bootstrap, proporcionando uma experiência interativa e bem estruturada ao usuário.
5. O backend em Python define a lógica do aplicativo e realiza a extração de texto dos arquivos enviados.
6. O texto extraído é processado pela API Azure OpenAI, que utiliza o GPT-4 para gerar os resumos, análises e descrições.

## Configuração do Projeto

### Pré-requisitos

- Python 3.6+
- Conta na Azure com a API Azure OpenAI habilitada
- Conta no ImgBB para hospedagem de imagens

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/sauloleite/File-Analyzer-with-Flask-and-Azure-OpenAI.git
   cd seu-repositorio
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
### Configuração das Chaves, Endpoints e Implatações
Insira no código as chaves da OpenAI e da ImgBB e o endpoint da sua chave Azure nestas linhas do código app.py:
```python
# Configuração da API da OpenAI
client = AzureOpenAI(
    azure_endpoint="insira_aqui_o_endpoint_da_sua_chave_azure",
    api_key='insira_aqui_a_sua_chave_azure',
    api_version="insira_aqui_a_versao_da_api" #Como sugestão, use: "2024-02-01"
)
```
Insira a API Key de imgbb neste trecho do código app.py:
```python
def upload_image_to_imgbb(image_bytes):
    imgbb_api_key = 'insira_aqui_a_sua_chave_imgbb'
```

Insira a nome da implantação do modelo da openAI nestes trechos do código app.py:
```python
response = client.chat.completions.create(
        model="insira_aqui_a_implementação_do_modelo_da_openai"
```
## Executando a Aplicação

Para iniciar o servidor Flask, execute:

```bash
flask run
```

Acesse o aplicativo no navegador através do endereço:
```bash
http://127.0.0.1:5000/
```

Na primeira execução, será solicitada uma autenticação:
Login: admin
Senha: admin321

## Subindo aplicação no Azure
1. Depois de realizar as alterações, crie um repositório da sua aplicação, no github, por exemplo.
2. Realize o login no portal.azure.com.
3. Abra o "Azure Cloud Shell"
4. Clone sua aplicação com comando
  ```bash
   git clone link_do_seu_repositório_aqui.git
   cd nome_do_seu_repositório
  ```
5. Execute este comando:
  ```bash
az webapp up --name nome_do_seu_webapp_aqui
  ```
6. Clique no link gerado e sua aplicação estará pronta para ser consumida

   
### Estrutura dos Arquivos
- app.py: Script principal da aplicação Flask.
- templates/: Contém os arquivos HTML (index.html e result.html).
- static/: Contém arquivos estáticos como CSS e imagens.

### Funcionalidades

1. Envio de Arquivos: Usuários podem enviar arquivos .docx, .pdf, .txt, .pptx, .png, .jpg, .jpeg para análise.
2. Extração de Conteúdo: Extração de texto e imagens dos arquivos enviados.
3. Processamento com OpenAI: Utiliza a API Azure OpenAI para gerar resumos, análises e descrições do conteúdo extraído.
4. Hospedagem de Imagens: Imagens são hospedadas no ImgBB temporariamente e descritas utilizando a OpenAI.
5. Interface Interativa: Desenvolvida com HTML, CSS, JS e Bootstrap.

### Contato
Para dúvidas ou suporte, entre em contato pelo email: sjoldeveloper@gmail.com

