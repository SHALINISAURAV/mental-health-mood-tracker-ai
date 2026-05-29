import streamlit as st
from ui.sidebar import render_sidebar

from models.inference import predict_emotion

from database.schema import create_tables
from database.crud import save_journal

from ui.custom_css import CUSTOM_CSS

from ui.components import (
    render_hero,
    feature_card
)
from ui.dashboard import (
    render_dashboard_metrics
)

from suggestions.recommendation_engine import (
    generate_recommendations
)

from suggestions.emergency_support import (
    detect_emergency
)

# =========================================
# CREATE DATABASE TABLES
# =========================================

create_tables()

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="MoodMind AI",
    page_icon="🧠",
    layout="wide"
)

# =========================================
# LOAD GLOBAL CSS
# =========================================

st.markdown(
    CUSTOM_CSS,
    unsafe_allow_html=True
)

# =========================================
# SIDEBAR
# =========================================

render_sidebar()

# =========================================
# HERO SECTION
# =========================================

render_hero()

st.write("")

# =========================================
# FEATURE CARDS
# =========================================

col1, col2, col3 = st.columns(3)

with col1:

    feature_card(
        "😊 Emotion Detection",
        "Detect emotions using transformer-based NLP models."
    )

with col2:

    feature_card(
        "📊 Mood Analytics",
        "Track emotional trends and behavioral patterns."
    )

with col3:

    feature_card(
        "🧘 Wellness Insights",
        "Receive personalized AI wellness suggestions."
    )

# =========================================
# JOURNAL SECTION
# =========================================

st.write("")
st.write("")

st.markdown("## ✍️ Write Today's Journal")

journal_text = st.text_area(
    "How are you feeling today?",
    height=220,
    placeholder="Write your thoughts here..."
)

# =========================================
# ANALYZE BUTTON
# =========================================

if st.button("Analyze Emotion"):

    # =========================================
    # VALIDATION
    # =========================================

    if journal_text.strip() == "":

        st.warning("Please write something first.")

    else:

        # =========================================
        # EMERGENCY DETECTION
        # =========================================

        if detect_emergency(journal_text):

            st.error(
                "⚠️ Your journal indicates emotional distress."
            )

            st.info(
                "Please consider reaching out to a trusted "
                "person or mental health professional."
            )

        with st.spinner("Analyzing emotions..."):

            # =========================================
            # RUN AI MODEL
            # =========================================

            predictions = predict_emotion(
                journal_text
            )

            # =========================================
            # SORT PREDICTIONS
            # =========================================

            predictions = sorted(
                predictions,
                key=lambda x: x["score"],
                reverse=True
            )

            # =========================================
            # TOP EMOTION
            # =========================================

            top_emotion = predictions[0]
            
            # =========================================
            # DASHBOARD METRICS
            # =========================================

            render_dashboard_metrics(
            total_entries=1,
            top_emotion=top_emotion["label"]
)

            # =========================================
            # GENERATE AI RECOMMENDATIONS
            # =========================================

            recommendations = generate_recommendations(
                top_emotion["label"]
            )

            # =========================================
            # SAVE TO DATABASE
            # =========================================

            save_journal(
                text=journal_text,
                emotion=top_emotion["label"],
                confidence=top_emotion["score"]
            )

            # =========================================
            # DISPLAY TOP EMOTION
            # =========================================

            st.markdown(
                f"""
                <div class="emotion-box">

                    <h2>
                        🎯 Detected Emotion:
                        {top_emotion['label'].capitalize()}
                    </h2>

                    <p>
                        Confidence Score:
                        {top_emotion['score']:.2f}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            # =========================================
            # EMOTION SCORES
            # =========================================

            st.subheader(
                "📈 Emotion Confidence Scores"
            )

            for emotion in predictions:

                st.write(
                    f"### {emotion['label'].capitalize()}"
                )

                st.progress(
                    float(emotion["score"])
                )

                st.write(
                    f"Confidence: "
                    f"{emotion['score']:.2f}"
                )

                st.write("")

            # =========================================
            # AI WELLNESS RECOMMENDATIONS
            # =========================================

            st.subheader(
                "🤖 Personalized Wellness Suggestions"
            )

            # Coping Strategies

            for strategy in recommendations["strategies"]:

                st.success(strategy)

            # Wellness Tip

            st.info(
                f"🌿 Wellness Tip: "
                f"{recommendations['wellness_tip']}"
            )