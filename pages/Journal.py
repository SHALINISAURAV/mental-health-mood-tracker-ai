import streamlit as st

st.set_page_config(
    page_title="Journal | MoodMind AI",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ Daily Journal")

st.write("Write your thoughts and let AI analyze your emotions.")

journal_text = st.text_area(
    "How are you feeling today?",
    height=250,
    placeholder="Write freely here..."
)

if st.button("Analyze Emotion"):
    if journal_text.strip() == "":
        st.warning("Please write something.")
    else:
        st.success("Emotion analysis will come in next phase 🚀")