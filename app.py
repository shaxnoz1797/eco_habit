import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from eco_agent import client

load_dotenv()


st.title("EcoHabit AI Agent 🌿")

if st.button("AI Tahlilini olish"):
    try:
        response = client.generate_content("Ekologik odatlar haqida qisqa maslahat ber.")
        st.success("AI javob berdi:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Xatolik: {e}")

st.markdown("---")
st.caption("EcoHabit Project - AI Dashboard v1.0")