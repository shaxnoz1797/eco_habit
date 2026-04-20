import streamlit as st

from eco_agent import client

st.title("Loyiha holatini tekshirish")

try:
    # MUHIM: .models so'zini olib tashladik, chunki client allaqachon model hisoblanadi
    response = client.generate_content(
        contents="Salom, loyihani tugatishimga yordam ber!"
    )

    st.success("✅ MUAMMO HAL BO'LDI!")
    st.write("AI javobi:")
    st.write(response.text)

except Exception as e:
    st.error("❌ Xatolik yuz berdi:")
    st.write(e)