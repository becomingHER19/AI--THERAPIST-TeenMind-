import streamlit as st
import speech_recognition as sr
import pyttsx3

st.set_page_config(page_title="LexiAI", layout="centered")

st.markdown("""
    <style>
        .main {
            background: linear-gradient(to bottom right, #e8f5e9, #ffffff);
        }
        h1, h2, h3 {
            color: #2e7d32;
        }
        .stButton>button {
            background-color: #2e7d32;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📖 LexiAI – Your Reading Buddy")
st.write("A simple AI assistant to help young learners improve their reading and comprehension.")

st.header("🎤 Read-Along Mode")
if st.button("Start Listening"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
        except:
            st.error("Sorry, I couldn't understand. Try again.")

st.header("🧠 Comprehension Check")
question = "What is the main idea of the story you just read?"
st.write(f"**Q:** {question}")
answer = st.text_input("Type your answer:")
if answer:
    st.success("Awesome! Keep going!")

st.header("🗣️ Voice Support")
tts_text = st.text_input("Enter text to read aloud:")
if st.button("Speak"):
    engine = pyttsx3.init()
    engine.say(tts_text)
    engine.runAndWait()
    st.success("Text spoken!")

st.header("📊 Progress Tracker (Coming Soon)")
st.info("Track your reading time, mistakes, and improvements here.")
