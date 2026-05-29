import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown("## 🧠 MoodMind AI")

        st.write("AI-powered emotional wellness platform")

        st.divider()

        st.markdown("## 🚀 Navigation")

        st.write("🏠 Home")
        st.write("📜 History")
        st.write("📊 Analytics")

        st.divider()

        st.markdown("## ✨ Features")

        st.write("✅ Emotion Detection")
        st.write("✅ Behavioral Analytics")
        st.write("✅ AI Recommendations")
        st.write("✅ Journal Tracking")
        st.write("✅ Emotional Insights")

        st.divider()

        st.markdown("💜 Made with Streamlit + AI")