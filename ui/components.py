import streamlit as st

# =========================================
# HERO SECTION
# =========================================

def render_hero():

    st.markdown(
        """
        <div>

            <p class="hero-title">
                🧠 MoodMind AI
            </p>

            <p class="hero-subtitle">
                Emotion-aware journaling and
                behavioral analytics system
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================
# FEATURE CARD
# =========================================

def feature_card(title, description):

    st.markdown(
        f"""
        <div class="glass-card">

            <h3>{title}</h3>

            <p>{description}</p>

        </div>
        """,
        unsafe_allow_html=True
    )