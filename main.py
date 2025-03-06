import streamlit as st
import google.generativeai as genai
import os

# Set up the Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyC3SF7bU8hd04TUdlnnZ2439EkAd7qK7BQ"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro")


def language_translate(text, source_lang, target_lang):
    prompt = f"""
    Translate the following text from {source_lang} to {target_lang}:

    {text}


    please don't add extra text, only translated text
    """
    response = model.generate_content(prompt)
    return response.text if response else "Translation failed."


st.title("Language Translator using Gemini AI")
user_text = st.text_area("Enter you text...")
selected_lang = ['English','Urdu','Hindi','Turkish','Chines']
source_lang = st.selectbox("choose source language",selected_lang)
target_lang = st.selectbox("choose target language",selected_lang)
if st.button("Translate"):
    if user_text.strip():
        translation = language_translate(user_text,source_lang,target_lang)
        st.subheader("Translated Text:")
        st.write(translation)
    else:
        st.warning("Please Enter text to translate")
st.title("Thank you")