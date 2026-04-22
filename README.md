🌍 EcoHabit: AI-Agentic Sustainable Habit Tracker
EcoHabit is a next-generation habit tracking dashboard that integrates OpenClaw AI Agents to verify and analyze sustainable actions. Built for the OpenClaw Challenge & 100 Days of Solana.

📺 Project Demo Video
EcoHabit Demo Video https://youtu.be/lq6IXVQx-5I

✨ Features

AI-Driven Verification: Uses an OpenClaw agent to browse the web and confirm eco-friendly facts.
Intelligent Analysis: Integrated with Google Gemini 1.5 Flash to provide personalized summaries of daily eco-tasks.
Browser Automation: Leverages Playwright to mimic human-like research for verification.
Gamified Dashboard: A "Soft UI" design with an Eco-Score and Leaderboard to encourage community engagement.


🏗️ Technical Architecture

User Side: A Django-based dashboard where users manage their habits.
Agent Side: An OpenClaw agent running a Playwright browser.
The Bridge: A custom REST API that allows the Agent to securely update the Dashboard status.


🛠️ Tech Stack

AI Model: Google Gemini 1.5 Flash (via Google AI Studio)
Frameworks: Django 5.x & Streamlit
Agent Framework: OpenClaw
Automation: Playwright (Chromium)
Blockchain: Solana (100 Days of Solana Challenge)
Styling: Custom CSS (Minimalist/Soft UI)


🔧 Installation & Setup

Clone the repo:
git clone https://github.com/shaxnoz1797/eco_habit.git