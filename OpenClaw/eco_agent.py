import os
import requests
import asyncio
import google.generativeai as genai
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

# API Kalitni sozlash
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


# 🧠 ISHLAYDIGAN MODELNI AVTOMATIK TOPISH FUNKSIYASI
def find_working_model():
    print("🔍 Sizning API kalitingiz uchun ishlaydigan model qidirilmoqda...")
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        print(f"📋 Topilgan modellar: {available_models}")

        # Ustuvorlik bo'yicha qidiramiz
        priority_list = ['models/gemini-1.5-flash', 'models/gemini-1.5-flash-latest', 'models/gemini-pro',
                         'models/gemini-1.0-pro']

        for target in priority_list:
            if target in available_models:
                return target

        # Agar ro'yxatdagilar bo'lmasa, birinchisini olamiz
        return available_models[0] if available_models else None
    except Exception as e:
        print(f"🚨 Modellarni olishda xato: {e}")
        return None


# Ishlaydigan modelni aniqlaymiz
WORKING_MODEL = find_working_model()

if not WORKING_MODEL:
    print("🚨 XATO: Hech qanday AI model topilmadi. API kalitni tekshiring.")
    exit()

model = genai.GenerativeModel(WORKING_MODEL)
API_URL = "http://127.0.0.1:8000/api/habit/1/done/"


async def run_ai_agent():
    print(f"🤖 OpenClaw AI Agent ({WORKING_MODEL} bilan) ishga tushdi...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print("🌐 DuckDuckGo'dan eko-ma'lumot qidirilmoqda...")
        await page.goto("https://duckduckgo.com/?q=eko+maslahatlar+uzbekistan+2024")

        try:
            await page.wait_for_selector("article", timeout=10000)
            results = await page.locator("article").all()
            text_to_analyze = ""
            for i in range(min(len(results), 2)):
                text_to_analyze += await results[i].inner_text() + "\n"

            print(f"📄 Matn tahlilga tayyor. Uzunligi: {len(text_to_analyze)}")

            print("🧠 AI tahlil qilmoqda...")
            prompt = f"Mana bu eko-yangilikni bitta qisqa o'zbekcha gap bilan xulosa qilib ber: {text_to_analyze}"

            # AI javobini olish
            response = model.generate_content(prompt)
            summary = response.text

            print(f"📝 AI Xulosasi: {summary}")

            # Djangoga yuborish
            print("🚀 Dashboardga yuborilmoqda...")
            res = requests.post(API_URL, json={"description": summary})

            if res.status_code == 200:
                print("🌟 MUVAFFAQIYAT! Dashboard yangilandi.")
            else:
                print(f"❌ Django xatosi: {res.status_code}")

        except Exception as e:
            print(f"🚨 Xato yuz berdi: {e}")

        print("⏳ 5 soniyadan keyin brauzer yopiladi...")
        await page.wait_for_timeout(5000)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(run_ai_agent())