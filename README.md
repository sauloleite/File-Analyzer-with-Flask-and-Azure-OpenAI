# File Analyzer with Flask and Azure OpenAI

This application is a WebApp that allows users to upload various types of files—such as documents, presentations, and images—for creating summaries, analyses, and descriptions using Azure services, including the Azure OpenAI API. It utilizes the multimodal capabilities of the GPT-4 model, enabling it to process and understand both text and images. This functionality makes it highly effective in handling diverse file formats and extracting meaningful insights from mixed content, thereby enhancing the overall utility and flexibility of the application in managing complex data inputs.


## Architecture

### Architecture Components

1. **Users:**
   - Upload files through the browser.

2. **Azure Resource:**
   - **Resource Group:** Grouping of services used in the architecture.
   - **App Service Plan:** Provides the foundation for the application's operation, offering the necessary underlying resources.
   - **App Service Web App:** Hosts the Python web application in a Linux server environment.

3. **Technologies Used:**
   - HTML, CSS, JS, Bootstrap: Technologies to create and style the user interface.
   - Python: Language for developing the application logic.
   - Flask: Framework used to structure the web application and provide basic features.
   - Azure OpenAI API: Processes the extracted texts using the GPT-4 language model to generate summaries, analyses, and descriptions.

### Step-by-Step Operation

1. Users upload files through the browser.
2. The App Service Plan provides infrastructure support for the WebApp.
3. The WebApp, hosted on the App Service Web App, uses Flask to manage the Python application.
4. The application interface is developed with HTML, CSS, JS, and Bootstrap, providing an interactive and well-structured experience to the user.
5. The Python backend defines the application logic and performs text extraction from the uploaded files.
6. The extracted text is processed by the Azure OpenAI API, which uses GPT-4 to generate the summaries, analyses, and descriptions.

## Project Setup

### Prerequisites

- Python 3.6+
- Azure account with Azure OpenAI API enabled
- ImgBB account for image hosting

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sauloleite/File-Analyzer-with-Flask-and-Azure-OpenAI.git
   cd your-repository

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

### Configuration of Keys, Endpoints, and Deployments
Obtaining Keys and Endpoints in Azure AI Services | OpenAI:
1. Log in to the Azure portal: portal.azure.com.
2. In the left navigation panel, click on "Create a resource" and search for "OpenAI".
3. Select "Azure OpenAI" and click "Create".
4. Choose the subscription, resource group, and desired region. Name your OpenAI resource and click "Review + create".
5. After creation, go to the OpenAI resource you created.
6. In the left navigation panel, click on "Keys and Endpoints".
7. Copy the "Key" and "Endpoint" values and insert them into the app.py code as follows:
   ```python
   # OpenAI API Configuration
   client = AzureOpenAI(
       azure_endpoint="insert_here_your_azure_endpoint",
       api_key='insert_here_your_azure_key',
       api_version="insert_here_the_api_version" # As a suggestion, use: "2024-02-01"
   )
   ```
Obtaining the ImgBB API Key and inserting it into the code:
1. Visit the ImgBB website: https://imgbb.com/.
2. If you do not have an account, create one. Otherwise, log in.
3. In the top right corner, click on your username and then on "Settings".
4. In the left menu, click on "API".
5. Click on "Add API key".
6. Name your API key and click "Create".
7. After creation, copy the value of your API Key.
8. Open the app.py file in your code editor.
9. Find the code snippet that defines the function upload_image_to_imgbb and replace 'insert_here_your_imgbb_key' with your ImgBB API Key that you copied:
   ```python
   def upload_image_to_imgbb(image_bytes):
       imgbb_api_key = 'insert_here_your_imgbb_key'
   ```

Deploying the Model in Azure OpenAI Studio:
1. In the Azure portal, navigate to the Azure OpenAI resource you created.
2. In the left navigation panel, click on "Models".
3. Click "Deploy a model".
4. Select the model you wish to deploy (for example, GPT-4).
5. Name your deployment and click "Create".
6. After the deployment, go to the "Deployments" section and copy the name of the deployment.
7. Insert the deployment name into the app.py code as follows:
   ```python
   response = client.chat.completions.create(
           model="insert_here_your_openai_model_deployment_name"
   ```
8. Save the changes to your project
   
## Running the Application

To start the Flask server, execute:

```bash
flask run
```

Access the application in the browser at:
```bash
http://127.0.0.1:5000/
```

On the first execution, authentication will be requested:
Login: admin
Password: admin321

## Deploying Application on Azure
1. After making changes, create a repository of your application, on GitHub, for example.
2. Log in to portal.azure.com.
3. Open the "Azure Cloud Shell".
4. Clone your application with the command:
     ```bash
      git clone your_repository_link_here.git
      cd your_repository_name
     ```
5. Execute this command:
     ```bash
      az webapp up --name your_webapp_name_here
     ```
6. Click on the generated link and your application will be ready to be consumed.

   
### File Structure
- app.py: Main Flask application script.
- templates/: Contains HTML files (index.html and result.html).
- static/: Contains static files such as CSS and images.

### Features

1. File Upload: Users can upload .docx, .pdf, .txt, .pptx, .png, .jpg, .jpeg files for analysis.
2. Content Extraction: Extracts text and images from the uploaded files.
3. Processing with OpenAI: Uses the Azure OpenAI API to generate summaries, analyses, and descriptions of the extracted content.
4. Image Hosting: Images are temporarily hosted on ImgBB and described using OpenAI.
5. Interactive Interface: Developed with HTML, CSS, JS, and Bootstrap.

### Contact
For questions or support, contact by email: sjoldeveloper@gmail.com


