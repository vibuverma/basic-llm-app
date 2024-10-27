from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image

import google.generativeai as genai


load_dotenv()  # take environment variables from .env


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# load gemini pro model
model = genai.GenerativeModel("gemini-1.5-flash")


# function to load gemini pro vision model and get response
def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:    # load gemini pro model
        response = model.generate_content(image)
    return response.text


# streamlit app
st.set_page_config(page_title="Gemini Pro Vision Chatbot", layout="wide")
st.header("Gemini Application")

input = st.text_input("Enter your prompt:", key="input")
# upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Image Description")

if submit:
    output = get_gemini_response(input,image)
    st.subheader("Image Description:")
    st.write(output)