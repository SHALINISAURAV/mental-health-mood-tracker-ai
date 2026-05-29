import streamlit as st


def render_sidebar():

    with st.sidebar:

        # =========================================
        # BRAND
        # =========================================
        st.markdown("## 🧠 MoodMind AI")
        st.caption("AI-powered emotional wellness platform")

        st.divider()

        # =========================================
        # NAVIGATION
        # =========================================
        st.markdown("### 🚀 Navigation")

        st.page_link("app.py", label="🏠 Home")
        st.page_link("pages/History.py", label="📜 History")
        st.page_link("pages/Analytics.py", label="📊 Analytics")

        st.divider()

        # =========================================
        # FEATURES
        # =========================================
        st.markdown("### ✨ Features")

        st.write("🧠 Emotion Detection")
        st.write("📊 Behavioral Analytics")
        st.write("🤖 AI Recommendations")
        st.write("📝 Journal Tracking")
        st.write("📈 Emotional Insights")

        st.divider()

        # =========================================
        # FOOTER
        # =========================================
        st.markdown("💜 Built with Streamlit + AI")