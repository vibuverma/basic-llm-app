# Streamlit Generative AI App

The Streamlit Generative AI App is a web application that leverages Google's generative AI models to create interactive and dynamic content. This app allows users to input text prompts or upload images, and generates AI-driven responses or descriptions based on the input. It is built using Streamlit, a Python library for creating web apps, and utilizes environment variables for secure API key management. The application is designed to demonstrate the capabilities of generative AI models in both text and vision domains, providing users with an easy-to-use interface for engaging with advanced AI technologies.

## Usage

To run the Streamlit Generative AI App, you can follow these steps:

1. Installing requirements:
```bash
    python -m pip install -r requirements.txt
```
2. Create `.env` file in root directory
3. Add your API Key in `.env` file
4. Running Text generation App
```bash
    streamlit run app.py
```
5. Running Image generation App
```bash
    streamlit run vision.py
```