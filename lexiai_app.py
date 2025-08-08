import streamlit as st

st.set_page_config(page_title="LexiAI", layout="centered")

st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
    }
    .big-title {
        font-size: 2rem;
        font-weight: 600;
        color: #2e7d32;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>👀 Ooooh you liked <b>LexiAI</b>? Say less — we can totally make that your winning pitch.</div>", unsafe_allow_html=True)

st.header("💡 Recap of the LexiAI Concept")
st.markdown("**LexiAI – A reading and comprehension assistant for students with dyslexia or learning difficulties.**")

st.header("🔥 Why LexiAI is a sleeper hit that could win the ₹15,000:")
criteria = {
    "✅ Relevance": "Learning disabilities are common and overlooked. India lacks tools to support these kids.",
    "✅ Clarity": "Easy to explain: “It helps kids read and understand better using voice + AI.”",
    "✅ Feasibility": "Use open-source voice recognition, text-to-speech tools, or even mockups.",
    "✅ Creativity": "Not cliché like “AI therapist.” Rarely anyone presents this in school-level events.",
    "✅ Impact": "Helps teachers, students, schools. Huge potential in EdTech or CSR.",
    "✅ Professionalism": "Clean, empathy-driven, and backed with logic — wins hearts and brains."
}
for key, value in criteria.items():
    st.markdown(f"**{key}**: {value}")

st.header("🧠 Bonus Strategy")
st.markdown("""
Instead of just calling it "for dyslexia," present it like:

> “A voice-based AI reading assistant to help **young learners with reading difficulties**, whether it's dyslexia, ADHD, or delayed literacy.”

✅ Broader use-case  
✅ No scary medical labels  
✅ Empathetic + inclusive
""")

st.header("📲 Features of LexiAI")
features = {
    "📖 Read-Along Mode": "The child reads aloud. LexiAI listens, offers corrections, praises efforts.",
    "🧠 Comprehension Check": "After reading, it asks simple Qs to check understanding.",
    "🗣️ Voice Support": "Uses text-to-speech to read out words, sentences, or even full stories.",
    "💬 Word Buddy": "Tells meaning and pronunciation of tough words in friendly tone.",
    "🌈 Custom Difficulty": "You can choose reading level based on age or fluency.",
    "📊 Progress Tracker": "Tracks reading time, errors, improvements (for teachers/parents)."
}
for key, value in features.items():
    st.markdown(f"**{key}**: {value}")

st.header("🎯 You can:")
st.markdown("""
- Show a **mock interface**  
- Add a **case study story**  
- End with: “We believe LexiAI can turn struggling readers into confident learners.”
""")
