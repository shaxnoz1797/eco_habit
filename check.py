from google import genai
import streamlit as st
from OpenClaw.eco_agent import client

api_key=st.secrets["GEMINI_API_KEY"]


try:

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents="Salom, loyihani tugatishimga yordam ber!"
    )

    print("✅ MUAMMO HAL BO'LDI!")
    print(response.text)
except Exception as e:
    print("❌ BU MODEL HAM LIMIT: 0 BERDI:")
    print(e)