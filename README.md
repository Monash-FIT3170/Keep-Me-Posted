# Keep-Me-Posted

**Keep Me Posted (KMP)** is a powerful web application designed to streamline your meeting processes by providing concise summaries of meeting discussions. KMP allows users to focus on productive conversations rather than wasting precious time documenting meeting minutes.

## Team Members (2024)


| **Product Owners**                              | **Release Train Engineers**                              | **System Architects**                              |
|-------------------------------------------------|------------------------------------------------|------------------------------------------------|
| **Danny Leung** <br> 32478704 |**Alex Ung** <br> 32498853 | **Ahmed Almasry** <br> 31130143|
| **Diya Ramesh** <br>  32336012 | **Maureen Pham** <br> 33117144 | **Harrison Lane** <br>  33110077 |
| **Afia Farzana** <br>  32501986 | **Zihao (Jeremy) Wang** <br>  32520433 | **Rohit Valanki** <br> 31451764 |
| **Ayesha Tariq** <br>  32497857 | **Benjamin Cherian** <br>  31483534 | **Brenda Dang** <br> 33111197 |
|**Parul Garg** <br> 32720254  |**Bowen Dong** <br>  33109834 | **Angelina Leung** <br> 33114447|
||**Marcus Wei** <br>  32503881 ||                                              |                                                 |

# Installation Guide

Follow these steps to set up and run the Keep Me Posted application locally.

If you are setting up KMP for the first time, please follow the instructions under **Installing and Running the Application**. Otherwise, follow the instructions under **Running the Application Only**.

## Prerequisite

Before running the application locally, ensure you have installed node and npm globally - [guide]( https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) 


## Installing and Running the Application
Ensure you are in the root directory.

### On Windows 
To install all requirements and run the application on Windows, execute the run_install.bat file. You can do this by double-clicking the file in your file explorer or by running the following command in your terminal:
```console
./run_install.bat
```

### On macOS
To install and run the servers on macOS, execute the run_install.sh script. Use the following command in your terminal:
```console
bash run_install.sh
```

## Running the Application Only
Ensure you are in the root directory.

### On Windows 
To run the application on Windows, execute the run.bat file. You can do this by double-clicking the file in your file explorer or by running the following command in your terminal:
```console
./run.bat
```

### On macOS
To run the servers on macOS, execute the run.sh script. Use the following command in your terminal:
```console
bash run.sh
```

# Hardware and Software Required

## Hardware 
The project can be run on any machine. MacOS and Windows have shell scripts that can be used to run the project locally.

## Software

### Frontend
Sveltekit is used for the frontend. SvelteKit is a framework for rapidly developing robust, performant web applications using Svelte. Svelte is a tool for building web applications. Like other user interface frameworks, it allows you to build your app declaratively out of components that combine markup, styles and behaviours. These components are compiled into small, efficient JavaScript modules that eliminate overhead traditionally associated with UI frameworks. A Svelte tutorial document was created in the process of building the application - [guide](https://docs.google.com/document/d/17psSA8k25k4564wV-8v7a0rGIPiNH81VshTD11CCbUA/edit#heading=h.9ezp793n1bwb). Other tutorials can be found for Svelte - [guide](https://learn.svelte.dev/tutorial/welcome-to-svelte), and SvelteKit - [guide](https://kit.svelte.dev/docs/introduction). For our application we are using SvelteKit version 3.0.0.

### Backend
Django is used for the backend. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. A Django tutorial document was created in the process of building the application - [guide](https://docs.google.com/document/d/1YI8r4dVbv2plGCXqexPKSkVPoaYwnvzpAtN_q0XUfro/edit#heading=h.9ezp793n1bwb). Other tutorials can be found for Django - [guide](https://docs.djangoproject.com/en/5.1/). For our application we are using Django version 5.0.4.

# Required APIs
1. Add a **.env file** to the **KEEP-ME-POSTED** root directory.
2. Add a **.env.local file** to the **frontend** directory.
3. Add the paths for these 2 files to **.gitignore** (these files must NOT be pushed to Git).
## Google Gemini
1. Generate an API key (see [here](https://ai.google.dev/gemini-api/docs/api-key)) and put it in the **.env file** in the following format:

    ```
    GEMINI_API_KEY = "insert API key here"
    ```

2. Click on the project in Google Cloud Console and generate OAuth client IDs by clicking "Create Credentials".

3. Add the IDs to the **.env.local file** in the following format (without the curly brackets):

    ```
    VITE_SECRET_CLIENT_ID={insert ID here}

    VITE_SECRET_CLIENT_SECRET={insert ID here}
    ```

## AssemblyAI
1. Generate an API key (see [here](https://www.assemblyai.com/products/speech-to-text?utm_source=google&utm_medium=cpc&utm_campaign=Brand&utm_term=assemblyai%20api&gad_source=1&gclid=CjwKCAjwuMC2BhA7EiwAmJKRrI_UILFgqbguYibYz-ycmPIH38b_nN6eS8sUZX0ES2pGG_A2ldjJSxoC22IQAvD_BwE)) and put it in the **.env file** in the following format:

    ```
    ASSEMBLYAI_API_KEY="insert API key here"
    ```

## SMTP
1. Create a Google account.
2. Enable 2-factor authentication and generate a pass key (see [here](https://www.youtube.com/watch?v=RlfyGCxuNVI)) and put it in the **.env file** in the following format:

    ```
    SMTP_EMAIL = "your google email address"
    SMTP_API_KEY = "insert pass key here"
    ```

## Google Cloud Platform
1. Create a Google Cloud Platform account.
2. Create a new project.
3. Under **APIs and Services**, go to **OAuth** consent screen.
4. Set type to external, fill in required fields, and continue.
5. Skip over scopes.
6. In the **Test Users** page, add the emails of the people who will need to have access to the Google services using your app for development (the services will be blocked to emails not added here unless you submit your app to google for review). Additional emails can be added later on (up to 100 test users).
7. In APIs, under credentials, click **Create Credential -> OAuth client ID**.
8. Select web application and add **“Authorized redirect URIs”**. These are the URLs that can send OAuth requests using your client ID and password. 
9. Once you create the ID you’ll be able to see **client ID and client secret**.
10. Create an API key (used in the google drive button component).
11. Go to enabled APIs and services and enable the following:
    - Google Drive API
    - Gmail API
    - People API
12. Add the keys to **.env.local**.

# Folder Structure of the Repository
A detailed explanation of the structure of the backend folder (Keep-Me-Posted/backend) can be found [here](https://docs.google.com/document/d/1YI8r4dVbv2plGCXqexPKSkVPoaYwnvzpAtN_q0XUfro/edit#heading=h.9ezp793n1bwb).

A detailed explanation of the structure of the frontend folder (Keep-Me-Posted/frontend) can be found [here](https://docs.google.com/document/d/17psSA8k25k4564wV-8v7a0rGIPiNH81VshTD11CCbUA/edit#heading=h.9ezp793n1bwb).


# Login Credentials
See [this link](https://docs.google.com/document/d/12utGqgSPGZd5jvaNlT22FTJlpHR073LqWaKULZvcidU/edit) for accounts for:
* AssemblyAI project
* Django admin account
* Gmail login

# UI/UX Prototyping
See [this link](https://www.figma.com/design/2ViXY8jjaYoqQUNvJ0zHOE/Keep-Me-Posted-Designs?node-id=2210-441096&t=XM3WtZ90aTzj3E8g-1) to edit and view the Figma.

# Developer Notes and Common Bugs
## Notes
### Adhering to Privacy Policy
The current version of KMP is subject to the *SMTP Privacy Policy* and *Google Gemini’s Generative-AI Prohibited Use Policy*, which both do not allow users under the age of 18 to access their services. Currently, KMP allows users aged 13 and above to be able to generate AI-summaries and send it through email. Before its professional release, authentication must ensure only adults aged 18 and above are allowed to use KMP and its services to comply with the privacy policies of the third-party services mentioned prior.
### AssemblyAI Speech-to-Text API
As of August 2024, AssemblyAI’s Speech-to-Text API imposes a usage and concurrency limit on its free tier. Please keep in mind that this usage limit may be partially expended if you decide to use the AssemblyAI project and account found in the “Login Credentials” section above - the account listed is under the free plan and is not paid.

## Common Bugs and Responses
| **Description**                              | **Counter Measures**                              |
|----------------------------------------------|---------------------------------------------------|
|Cache files found in .gitignore may be accidentally pushed to the repository. These will come up under “Unstaged Changes” under Source Control when you run the code locally. Examples of these cache files include non-ambient.d.ts and db.sqlite3. | In the case where the cache files are pushed to the Git repository by accident: Ensure all teammates run the following commands in the terminal - ```git clean -fxdn``` (to preview the files to be deleted) and then ```git clean -fxd``` (to confirm deletion). Alternatively, you can try to revert the commit by following [this](https://www.youtube.com/watch?v=H2DuJNWbqLw&t=70s) tutorial.|

# Guidance on Testing Pipeline
## Continuous Integration
Continuous integration of the frontend is implemented using Cypress. The relevant test cases can be found in the directory **frontend/cypress**. 

Cypress tests are recorded using cypress cloud (optional). The key is stored in the GitHub repository secret variables.

Continuous integration of the backend is implemented using Django’s built-in testing. The test cases can be found in the **backend/app_name/tests.py** file within the folder of each app in the backend.

GitHub Actions is used to run the test suite upon each pull request to either main or develop. GitHub Actions configurations can be found in the **.github/workflows** directory.

## Continuous Deployment
Continuous deployment of the frontend is supported by Netlify - every merge to the production branch in the Git repository is automatically deployed. Netlify also supports deployment of preview branches on every pull request which can be used for testing functionality before merging. Production branch can be changed in Netlify under **Site Configuration -> Continuous Deployment**.

Currently, there is no continuous deployment for the backend. The backend must be manually re-deployed on Render.