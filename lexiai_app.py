import streamlit as st
import speech_recognition as sr
import pyttsx3
import json
import os
import time

st.set_page_config(page_title="LexiAI", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "progress" not in st.session_state:
    st.session_state.progress = {"attempts": 0, "correct": 0, "speed": []}

# Text-to-speech
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognition
recognizer = sr.Recognizer()
def recognize_speech():
    with sr.Microphone() as source:
        st.info("🎤 Listening... Please speak now.")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            return recognizer.recognize_google(audio)
        except:
            return ""

# Pages
if st.session_state.page == "home":
    st.markdown("""
        <style>
            div[data-testid="stAppViewContainer"] {
                background: linear-gradient(to bottom right, #e0f7fa, #ffffff);
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("👀 Ooooh you liked LexiAI? Say less — we can totally make that your winning pitch.")
    st.markdown("**LexiAI – A reading and comprehension assistant for students with dyslexia or learning difficulties.**")
    if st.button("🚀 Enter Dashboard"):
        st.session_state.page = "dashboard"
        st.experimental_rerun()

elif st.session_state.page == "dashboard":
    st.sidebar.title("LexiAI Dashboard")
    choice = st.sidebar.radio("Select a tool:", ["📖 Read-Along", "🧠 Comprehension", "🗣️ AI Voice Reader", "💬 Word Buddy", "📊 Progress Tracker"])

    if choice == "📖 Read-Along":
        level = st.selectbox("Choose Reading Level:", ["Beginner", "Intermediate", "Advanced"])
        texts = {
            "Beginner": "The sun is hot.",
            "Intermediate": "Reading helps us learn more.",
            "Advanced": "Innovation in education empowers young minds."
        }
        target_text = texts[level]
        st.write("Read this aloud:")
        st.info(target_text)
        if st.button("🎤 Record & Check"):
            start = time.time()
            result = recognize_speech()
            end = time.time()
            st.write("You said:", result)
            st.session_state.progress["attempts"] += 1
            st.session_state.progress["speed"].append(round(end - start, 2))
            if result.lower().strip() == target_text.lower().strip():
                st.success("✅ Correct! Well read.")
                st.session_state.progress["correct"] += 1
            else:
                st.error("🔁 Not a match. Try again.")

    elif choice == "🧠 Comprehension":
        paragraph = st.text_area("Paste the paragraph you read:")
        if paragraph:
            st.write("AI-generated questions:")
            if "sun" in paragraph.lower():
                st.radio("What is hot?", ["The sun", "The moon", "The cloud"])
            elif "reading" in paragraph.lower():
                st.radio("What helps us learn?", ["Watching", "Reading", "Sleeping"])
            elif "education" in paragraph.lower():
                st.radio("What empowers young minds?", ["Games", "Education", "Food"])

    elif choice == "🗣️ AI Voice Reader":
        user_input = st.text_area("Paste any paragraph or word to read out loud:")
        if st.button("🔊 Read it Out"):
            speak(user_input)
            st.success("Spoken successfully!")

    elif choice == "💬 Word Buddy":
        word = st.text_input("Enter a word to define and pronounce:")
        definitions = {
            "sun": "The star at the center of the solar system.",
            "education": "The process of receiving or giving systematic instruction.",
            "innovation": "A new method, idea, or product."
        }
        if word:
            st.info(f"Definition: {definitions.get(word.lower(), 'Definition not found.')}")
            if st.button("🔊 Speak Word"):
                speak(word)

    elif choice == "📊 Progress Tracker":
        st.metric("Total Attempts", st.session_state.progress["attempts"])
        st.metric("Correct Readings", st.session_state.progress["correct"])
        if st.session_state.progress["speed"]:
            avg_speed = sum(st.session_state.progress["speed"]) / len(st.session_state.progress["speed"])
            st.metric("Avg. Reading Speed (sec)", round(avg_speed, 2))
        else:
            st.write("No speed data yet.")

    if st.sidebar.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.experimental_rerun()
