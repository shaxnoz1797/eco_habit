import google.generativeai as genai
import streamlit as st

from app import model

# Clientni tashqarida yarating, shunda boshqa fayllar uni import qila oladi
api_key = st.secrets.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
client = genai.GenerativeModel('gemini-1.5-flash')



def run_eco_agent():
    try:
        response = model.generate_content("Ekologik odatlar haqida tahlil ber...")
        st.write(response.text)
    except Exception as e:
        st.error(f"Xato yuz berdi: {e}")

if __name__ == "__main__":
    run_eco_agent()