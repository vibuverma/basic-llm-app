from dotenv import load_dotenv
import os
import streamlit as st

import google.generativeai as genai


load_dotenv()  # take environment variables from .env


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# load gemini pro model
model = genai.GenerativeModel("gemini-pro")


# function to load gemini pro model and get response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# streamlit app
st.title("Gemini Pro Chatbot")
st.set_page_config(page_title="Gemini Pro Chatbot", layout="wide")
st.header("Gemini LLM Application")