import google.generativeai as genai
import streamlit as st

# 1. API kalitni sozlash
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 2. Modelni yaratamiz
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat tarixi uchun xotira
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eski xabarlarni chiqarish
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Foydalanuvchi kiritishi
if prompt := st.chat_input("Savolingizni yozing..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:

            response = model.generate_content(prompt)

            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Xatolik: {e}")
            if "429" in str(e):
                st.warning("Eslatma: Qayerdadir baribir 2.5-flash qolib ketgan. Hamma fayllarni tekshiring.")