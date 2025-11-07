import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# =====================================================
# 1️⃣ Load API Key
# =====================================================
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# =====================================================
# 2️⃣ Hàm gọi Gemini API
# =====================================================
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

# =====================================================
# 3️⃣ Giao diện Streamlit
# =====================================================
st.set_page_config(page_title="AI English Assistant 🇬🇧", page_icon="🧠", layout="wide")

st.title("🧠 AI English Learning Assistant 🇬🇧")
st.write("Practice writing, get grammar feedback, and learn from your mistakes — powered by Google Gemini!")

# Tabs: Chat | Writing Correction | Quiz Generator
tab1, tab2, tab3 = st.tabs(["💬 Chat", "📝 Writing Correction", "🎯 Mini Quiz"])

# =====================================================
# 4️⃣ TAB 1: Chat học tiếng Anh
# =====================================================
with tab1:
    st.subheader("💬 Practice English Conversation")
    user_input = st.text_area("Say something or ask a question in English:", key="chat_input")

    if st.button("Send", key="chat_button"):
        if user_input.strip() == "":
            st.warning("Please enter a message!")
        else:
            with st.spinner("Gemini is thinking..."):
                prompt = f"You are a friendly English tutor. Reply in English, correct mistakes politely, and keep the tone encouraging.\n\nStudent: {user_input}"
                answer = ask_gemini(prompt)
                st.markdown(f"**Tutor:** {answer}")

# =====================================================
# 5️⃣ TAB 2: Writing Correction
# =====================================================
with tab2:
    st.subheader("📝 Improve Your Writing Skills")
    essay = st.text_area("Enter your English paragraph:")

    if st.button("Check Grammar", key="check_button"):
        if essay.strip() == "":
            st.warning("Please enter your text!")
        else:
            with st.spinner("Analyzing your writing..."):
                prompt = f"""
                You are an English teacher. 
                Correct the following student's writing. 
                Then provide:
                1. The corrected version.
                2. A list of grammar mistakes (with explanations in simple English and short Vietnamese).
                3. 3 example sentences to practice similar structures.
                Student writing:
                {essay}
                """
                answer = ask_gemini(prompt)
                st.markdown("### ✨ Feedback")
                st.write(answer)

# =====================================================
# 6️⃣ TAB 3: Mini Quiz Generator
# =====================================================
with tab3:
    st.subheader("🎯 Generate a Quick English Quiz")
    topic = st.text_input("Enter a topic (e.g., travel, food, technology):")

    if st.button("Generate Quiz", key="quiz_button"):
        if topic.strip() == "":
            st.warning("Please enter a topic!")
        else:
            with st.spinner("Creating quiz..."):
                prompt = f"""
                Create a short 5-question English quiz about the topic '{topic}'. 
                Include multiple-choice questions with 4 options and mark the correct answer.
                """
                quiz = ask_gemini(prompt)
                st.markdown("### 🧩 Quiz")
                st.write(quiz)

st.markdown("---")
st.caption("Built with ❤️ by Thai Nguyen using Streamlit + Google Gemini API")
