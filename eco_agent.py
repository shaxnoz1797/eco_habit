import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Modelni yaratamiz
client = genai.GenerativeModel('gemini-1.5-flash')

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


client = genai.GenerativeModel('gemini-1.5-flash')

def run_eco_agent():
    try:
        # Ishlayotgan modelni yozamiz
        response = client.generate_content(
           contents="Ekologik odatlar haqida tahlil ber..."
        )
        st.write(response.text)
    except Exception as e:
        print(f"Xato: {e}")

if __name__ == "__main__":
    run_eco_agent()