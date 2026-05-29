import streamlit as st

from ui.custom_css import CUSTOM_CSS
from ui.sidebar import render_sidebar
from ui.components import render_hero, feature_card
from ui.dashboard import render_dashboard_metrics

from models.inference import predict_emotion

from database.schema import create_tables
from database.crud import save_journal

from suggestions.recommendation_engine import generate_recommendations
from suggestions.emergency_support import detect_emergency


# ===============================
# PAGE CONFIG (FIRST LINE RULE)
# ===============================
st.set_page_config(
    page_title="MoodMind AI",
    page_icon="🧠",
    layout="wide"
)

# ===============================
# INIT DB (ONLY ONCE)
# ===============================
create_tables()

# ===============================
# LOAD CSS
# ===============================
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ===============================
# SIDEBAR
# ===============================
render_sidebar()

# ===============================
# HERO
# ===============================
render_hero()

st.write("")

# ===============================
# FEATURE CARDS
# ===============================
col1, col2, col3 = st.columns(3)

with col1:
    feature_card("😊 Emotion Detection", "Detect emotions using AI models.")

with col2:
    feature_card("📊 Mood Analytics", "Track emotional trends over time.")

with col3:
    feature_card("🧘 Wellness Insights", "Get personalized mental health tips.")

# ===============================
# JOURNAL INPUT
# ===============================
st.markdown("## ✍️ Write Today's Journal")

journal_text = st.text_area(
    "How are you feeling today?",
    height=220,
    placeholder="Write your thoughts here..."
)

# ===============================
# ANALYZE BUTTON
# ===============================
if st.button("Analyze Emotion"):

    if not journal_text.strip():
        st.warning("Please write something first.")
        st.stop()

    # emergency check
    if detect_emergency(journal_text):
        st.error("⚠️ Emotional distress detected")
        st.info("Please reach out to someone you trust ❤️")
        st.stop()

    with st.spinner("Analyzing emotions..."):

        predictions = predict_emotion(journal_text)

        predictions = sorted(
            predictions,
            key=lambda x: x["score"],
            reverse=True
        )

        top_emotion = predictions[0]

        # SAVE TO DB
        save_journal(
            text=journal_text,
            emotion=top_emotion["label"],
            confidence=top_emotion["score"]
        )

        # DASHBOARD
        render_dashboard_metrics(
            total_entries=1,
            top_emotion=top_emotion["label"]
        )

        # RECOMMENDATIONS
        recommendations = generate_recommendations(top_emotion["label"])

        if not recommendations:
            recommendations = {
                "strategies": [],
                "wellness_tip": "Take care of yourself 💜"
            }

        # RESULT UI
        st.markdown(f"""
        <div class="emotion-box">
            <h2>🎯 {top_emotion['label'].capitalize()}</h2>
            <p>Confidence: {top_emotion['score']:.2f}</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("📈 Emotion Scores")

        for e in predictions:
            st.progress(float(e["score"]))
            st.write(f"{e['label'].capitalize()} → {e['score']:.2f}")

        st.subheader("🤖 Recommendations")

        for s in recommendations["strategies"]:
            st.success(s)

        st.info(recommendations["wellness_tip"])