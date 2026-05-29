import streamlit as st

# =========================================
# HERO SECTION (CLEAN STREAMLIT)
# =========================================
def render_hero():

    st.markdown("## 🧠 MoodMind AI")

    st.caption(
        "Emotion-aware journaling and behavioral analytics system"
    )


# =========================================
# FEATURE CARD (CLEAN UI - NO HTML ISSUES)
# =========================================
def feature_card(title, description):

    with st.container():

        st.markdown(f"### {title}")
        st.write(description)

        st.divider()