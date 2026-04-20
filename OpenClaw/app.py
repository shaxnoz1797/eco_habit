import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

from eco_agent import client

# .env yuklash
load_dotenv()

# Sahifa sozlamalari
st.set_page_config(page_title="EcoHabit Dashboard", page_icon="🌱")

# Dashboard sarlavhasi
st.title("🌱 EcoHabit AI Agent")
st.markdown("---")



genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Modelni yaratamiz
model = genai.GenerativeModel('gemini-1.5-flash')


with st.sidebar:
    st.header("Sozlamalar")
    model_choice = st.selectbox("Modelni tanlang:", ["gemini-flash-lite-latest", "gemini-2.0-flash"])
    st.info("Bu agent ekologik odatlaringizni tahlil qiladi.")

# Ma'lumot +
user_input = st.text_input("Savolingizni yozing yoki 'Tahlil' tugmasini bosing:", "Ekologik odatlar haqida tahlil ber")

if st.button("Tahlilni boshlash"):
    with st.spinner("AI tahlil qilmoqda..."):
        try:
            # AI so'rovi
            response = client.models.generate_content(
                model=model_choice,
                contents=user_input
            )

            # Natijani
            st.subheader("🤖 AI Tahlili:")
            st.markdown(response.text)

            # Muvaffaqiyat xabari
            st.success("Tahlil yakunlandi!")

        except Exception as e:
            st.error(f"Xato yuz berdi: {e}")

# Footer
st.markdown("---")
st.caption("EcoHabit Project - AI Dashboard v1.0")