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
Obtenção das Chaves e Pontos de Extremidade no Azure AI Services | OpenAI:
1. Faça login no portal da Azure: portal.azure.com.
2. No painel de navegação esquerdo, clique em "Criar um recurso" e pesquise por "OpenAI".
3. Selecione "Azure OpenAI" e clique em "Criar".
4. Escolha a assinatura, o grupo de recursos e a região desejada. Dê um nome ao seu recurso OpenAI e clique em "Revisar + criar".
5. Após a criação, vá para o recurso OpenAI que você criou.
6. No painel de navegação esquerdo, clique em "Chaves e Endpoints".
7. Copie o valor da "Chave" e o "Endpoint" e insira-os no código app.py da seguinte forma:
   ```python
   # Configuração da API da OpenAI
   client = AzureOpenAI(
       azure_endpoint="insira_aqui_o_endpoint_da_sua_chave_azure",
       api_key='insira_aqui_a_sua_chave_azure',
       api_version="insira_aqui_a_versao_da_api" #Como sugestão, use: "2024-02-01"
   )
   ```
Obtenção da API Key do ImgBB e inserção no código:
1. Acesse o site do ImgBB: https://imgbb.com/.
2. Se ainda não tiver uma conta, crie uma. Caso contrário, faça login.
3. No canto superior direito, clique em seu nome de usuário e depois em "Settings".
4. No menu à esquerda, clique em "API".
5. Clique em "Add API key".
6. Dê um nome à sua chave API e clique em "Create".
7. Após a criação, copie o valor da sua API Key.
8. Abra o arquivo app.py no seu editor de código.
9. Encontre o trecho de código que define a função upload_image_to_imgbb e substitua 'insira_aqui_a_sua_chave_imgbb' pela sua chave API que você copiou do ImgBB:
   ```python
   def upload_image_to_imgbb(image_bytes):
       imgbb_api_key = 'insira_aqui_a_sua_chave_imgbb'
   ```

Implantação do Modelo no Estúdio do OpenAI do Azure:
1. No portal da Azure, navegue até o recurso Azure OpenAI que você criou.
2. No painel de navegação esquerdo, clique em "Modelos".
3. Clique em "Implantar um modelo".
4. Selecione o modelo que deseja implantar (por exemplo, GPT-4).
5. Dê um nome à sua implantação e clique em "Criar".
6. Após a implantação, vá para a seção "Implantações" e copie o nome da implantação.
7. Insira o nome da implantação no código app.py da seguinte forma:
   ```python
   response = client.chat.completions.create(
           model="insira_aqui_a_implementação_do_modelo_da_openai"
   ```
8. Salve as alterações do seu projeto
   
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
1. Depois de realizar as alterações, crie um repositório da sua aplicação, no github, por exemplo
2. Realize o login no portal.azure.com
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

