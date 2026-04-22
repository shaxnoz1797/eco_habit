import streamlit as st
import requests

import google.generativeai as palmed_genai # Kutubxona o'zgardi
from streamlit_lottie import st_lottie
import random
import google.generativeai as genai
import time
from google.api_core import exceptions


# --- 1.
st.set_page_config(page_title="EcoHabit AI Agent", page_icon="🌿", layout="wide")


# 1. API KEYNI SOZLASH

if "GEMINI_API_KEY" not in st.secrets:
    st.error("API Kalit topilmadi! .streamlit/secrets.toml faylini tekshiring.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# 2. MODELNI TANLASH
MODEL_NAME = 'gemini-1.5-flash'

try:
    model = genai.GenerativeModel(MODEL_NAME)
    st.success(f"Hozirgi ishlayotgan model: {MODEL_NAME}")
except Exception as e:
    st.error(f"Modelni yuklashda xato: {e}")


# 3. INTERFEYS
st.title("🤖 EcoHabit To'g'rilangan Bot")

user_input = st.text_input("Savol yozing:")

if st.button("Yuborish"):
    if user_input:
        try:


            response = model.generate_content(user_input)
            st.write("Javob:", response.text)
        except Exception as e:
            st.error(f"Xatolik yuz berdi: {e}")
            st.info("Agar xato 429 bo'lsa, demak kodingiz hali ham eski modelni qidiryapti.")




# --- 3. LOTTIE FUNKSIYASI ---
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)         # Timeout qo'shdik
        time.sleep(12)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_eco = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_5njp9v9m.json")



def generate_content_with_retry(model, prompt, max_retries=5):
    """
    Xatolik yuz berganda qayta urinish funksiyasi.
    """
    for attempt in range(max_retries):
        try:
            # So'rov yuborish
            response = model.generate_content(prompt)
            return response.text

        except exceptions.ResourceExhausted as e:
            # 429 xatoligi (Quota exceeded)
            wait_time = (2 ** attempt) * 10 + 5  # Har safar ko'proq kutish (15s, 25s, 45s...)
            print(f"Limitga yetildi ({attempt + 1}/{max_retries}). {wait_time} soniya kutilmoqda...")
            time.sleep(wait_time)

        except exceptions.ServiceUnavailable:
            # Server vaqtincha ishlamayotgan bo'lsa
            print("Server band. 5 soniyadan so'ng qayta urinib ko'riladi...")
            time.sleep(5)

        except Exception as e:
            # Boshqa kutilmagan xatoliklar
            print(f"Kutilmagan xatolik: {e}")
            break

    return "Xatolik tufayli javob olib bo'lmadi."


# --- 4. SIDEBAR ---
st.sidebar.divider()
st.sidebar.subheader("💡 Kun maslahati")

eco_tips = [
    "Plastik paket o'rniga matoli xaltadan foydalaning. 🛍️",
    "Kompyuterni kechasi o'chirib qo'ying, u 'vampir quvvat' sarflamasin. 💻",
    "Tish yuvayotganda suvni o'chirib qo'ying. 💧",
    "Qog'ozning ikki tarafidan ham foydalaning. 📝",
    "Xonadan chiqayotganda chiroqni o'chirishni unutmang. 💡",
    "Imkon bo'lsa, lift o'rniga zinadan foydalaning - bu ham salomatlik, ham energiya tejamkorligi! 🏃‍♂️"
]

# Sahifa har safar yangilanganda yangi maslahat chiqadi
random_tip = random.choice(eco_tips)
st.sidebar.info(random_tip)


st.sidebar.subheader("🎯 Sizning Eco-Progressingiz")


user_points = st.sidebar.slider("Bugun nechta ekologik ish qildingiz?", 0, 10, 3)

if user_points >= 7:
    st.sidebar.success("Siz bugun Ekologik Qahramonsiz! 🔥")
elif user_points >= 4:
    st.sidebar.warning("Yaxshi natija, yana ozgina harakat qiling! 🌱")
else:
    st.sidebar.info("Kichik qadamlar katta o'zgarishlarga olib keladi. 💪")
menu = st.sidebar.radio("Bo'limni tanlang:", ["Asosiy sahifa", "Energiya Kalkulyatori", "AI Agent bilan suhbat", "Biz haqimizda"])
if st.sidebar.button("🗑️ Suhbatni tozalash"):
    st.session_state.messages = []
    st.rerun()

# --- 5. BO'LIMLAR ---


# A) ASOSIY SAHIFA
if menu == "Asosiy sahifa":
    st.title("🌱 EcoHabit: Kelajakni birgalikda asraymiz")

    # Katta Banner (Hero Section)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Nega aynan EcoHabit?
        Bizning AI platformamiz sizga kundalik hayotingizda qanday qilib tabiatga kamroq zarar yetkazishni o'rgatadi. 
        Har bir kichik harakat — bu kelajak avlod uchun sovg'adir.
        """)
        if st.button("AI bilan gaplashishni boshlash 🚀"):
            # Bu tugma bosilganda AI bo'limiga o'tishni o'rgatamiz (bu biroz murakkab, hozircha shunchaki effekt)
            st.balloons()

    with col2:
        if lottie_eco:
            st_lottie(lottie_eco, height=250)

    st.divider()

    # Foydali ma'lumotlarni Expanders ichiga yashiramiz
    st.subheader("📚 Bilasizmi?")

    with st.expander("🔌 Kompyuterni o'chirmaslik qanchaga tushadi?"):
        st.write(
            "O'rtacha bir dona stol kompyuteri o'chirilmasdan qolsa, yiliga taxminan 150-200 kg CO2 chiqaradi. Bu 10 ta katta daraxt yutadigan karbonat miqdori!")

    with st.expander("♻️ Plastik haqida achchiq haqiqat"):
        st.write(
            "Bitta plastik paket tabiatda 400-500 yil davomida parchalanadi. Siz ishlatadigan matoli xalta esa 1000 martadan ortiq xizmat qiladi.")

    with st.expander("☀️ Qayta tiklanuvchi energiya"):
        st.write(
            "O'zbekistonda quyoshli kunlar ko'p. Quyosh panellari yordamida uyingizni bepul va toza energiya bilan ta'minlash mumkin.")



# B) KALKULYATOR
elif menu == "Energiya Kalkulyatori":
    st.title("📊 Energiya Kalkulyatori")
    c1, c2 = st.columns(2)
    with c1:
        device = st.selectbox("Qurilma:", ["Noutbuk", "Desktop PC"])
        hours = st.slider("Bo'sh turgan soatlar:", 0, 24, 8)
    with c2:
        price = st.number_input("1 kVt narxi (so'm):", value=600)

    watt = 50 if device == "Noutbuk" else 200
    saved_kwh = (watt * hours * 365) / 1000
    saved_money = saved_kwh * price

    st.divider()
    m1, m2 = st.columns(2)
    m1.metric("Yillik tejash (kVt)", f"{saved_kwh:.1f}")
    m2.metric("Yillik tejash (so'm)", f"{saved_money:,.0f}")



# C) AI AGENT (ASOSIY QISM)
elif menu == "AI Agent bilan suhbat":
    # st.title("🤖 EcoHabit Aqlli Yordamchi")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat tarixini chiqarish
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Savolingizni yozing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # 1. AKKAUNTINGIZDAGI ISHLAYDIGAN MODELLARNI RO'YXATI

                available_models = [m.name for m in palmed_genai.list_models() if
                                    'generateContent' in m.supported_generation_methods]

                # Eng yaxshi modelni tanlash (navbat bilan)
                target_model = None
                for m_name in ["models/gemini-1.5-flash", "models/gemini-pro", "gemini-1.5-flash", "gemini-pro"]:
                    if m_name in available_models:
                        target_model = m_name
                        break

                if not target_model:
                    # Agar yuqoridagilar topilmasa, ro'yxatdagi birinchisini olamiz
                    target_model = available_models[0]

                # 2. MODELNI ISHGA TUSHIRISH
                model = palmed_genai.GenerativeModel(target_model)

                # 3. JAVOB OLISH
                response = model.generate_content(
                    f"Siz EcoHabit loyihasining ekologiya mutaxassisiz. O'zbek tilida javob bering. Savol: {prompt}"
                )

                full_res = response.text
                st.markdown(full_res)
                st.session_state.messages.append({"role": "assistant", "content": full_res})
                st.caption(f"Ishlatilgan model: {target_model}")  # Qaysi model ishlaganini ko'rib turamiz

            except Exception as e:
                st.error(f"Xatolik yuz berdi: {str(e)}")
                st.info("Maslahat: Internetingiz yoki API kalitingizni tekshiring.")



# D) BIZ HAQIMIZDA
elif menu == "Biz haqimizda":
    st.title("📖 Loyiha haqida")
    st.write("Ushbu loyiha OpenClaw Challenge uchun tayyorlandi.")


st.markdown("---")
st.caption("EcoHabit Project - OpenClaw Challenge")