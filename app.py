import streamlit as st
import google.generativeai as genai


st.set_page_config(page_title="EcoHabit AI Agent", page_icon="🌿")



@st.cache_resource
def get_working_model():

    try:

        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)


        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]


        preferred_model = None
        for m_name in models:
            if "flash-latest" in m_name:
                preferred_model = m_name
                break

        if not preferred_model:
            for m_name in models:
                if "2.0-flash" in m_name:
                    preferred_model = m_name
                    break

        if not preferred_model:
            preferred_model = models[0]

        return genai.GenerativeModel(preferred_model), preferred_model
    except Exception as e:
        st.error(f"Modelni yuklashda xato: {e}")
        return None, None


model, model_name = get_working_model()


st.title("EcoHabit AI Agent 🌿")
if model_name:
    st.caption(f"Hozirgi ishlayotgan model: {model_name}")

user_habit = st.text_input("Bugungi odatingizni yozing (English):", placeholder="Example: I used a plastic bag today.")


if st.button("Agentni ishga tushirish"):
    if user_habit and model:


        with st.spinner("AI tahlil qilmoqda..."):
            try:
                prompt = f"""
                You are the EcoHabit AI Agent. 
                User input: '{user_habit}'.
                
                Tasks:
                1. Briefly explain the environmental impact.
                2. Suggest 3 eco-friendly alternatives.
                3. Give an 'Eco-Score' from 1 to 10.
                Respond in English.
                """
                response = model.generate_content(prompt)

                st.success("Tahlil yakunlandi!")
                st.markdown("---")
                st.markdown(response.text)
                st.balloons()
            except Exception as e:


                if "429" in str(e):

                    st.error("AI hozir juda band (Limit tugadi). Iltimos, 1 daqiqa kutib qayta urinib ko'ring.")
                else:

                    st.error(f"Xatolik yuz berdi: {e}")
    else:

        st.warning("Iltimos, ma'lumot kiriting!")



st.markdown("---")
st.caption("EcoHabit Project - OpenClaw Challenge")