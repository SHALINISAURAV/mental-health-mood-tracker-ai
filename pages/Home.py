import streamlit as st

st.set_page_config(
    page_title="Home | MoodMind AI",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# HERO SECTION
# -----------------------------

st.markdown(
    """
    <style>
    .hero-title {
        font-size: 60px;
        font-weight: bold;
        color: white;
    }

    .hero-subtitle {
        font-size: 24px;
        color: #cbd5e1;
    }

    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="hero-title">🧠 MoodMind AI</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="hero-subtitle">AI-powered emotional wellness and behavioral analytics system</p>',
    unsafe_allow_html=True,
)

# -----------------------------
# FEATURE SECTION
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="glass-card">
            <h2>😊 Emotion AI</h2>
            <p>Transformer-based emotion detection engine.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="glass-card">
            <h2>📊 Mood Analytics</h2>
            <p>Track emotional patterns and trends.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="glass-card">
            <h2>🧘 Wellness Insights</h2>
            <p>Get AI-generated coping recommendations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption("Built with ❤️ using Streamlit + Transformers")