import streamlit as st
import pandas as pd

from database.crud import fetch_journals

from analytics.charts import (
    create_emotion_pie_chart,
    create_emotion_timeline
)

from analytics.statistics import (
    calculate_total_entries,
    calculate_average_confidence
)

from analytics.trends import (
    get_most_common_emotion
)

from analytics.insights import (
    generate_behavioral_insight
)


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Analytics | MoodMind AI",
    page_icon="📊",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("📊 Mood Analytics Dashboard")

st.write(
    "Track emotional trends and behavioral patterns."
)

# =========================================
# FETCH DATABASE DATA
# =========================================

rows = fetch_journals()

# =========================================
# EMPTY STATE
# =========================================

if len(rows) == 0:

    st.info(
        "No journal data available yet."
    )

else:

    # =========================================
    # CREATE DATAFRAME
    # =========================================

    df = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Journal",
            "Emotion",
            "Confidence",
            "Created At"
        ]
    )

    # =========================================
    # METRICS
    # =========================================

    total_entries = calculate_total_entries(df)

    avg_confidence = calculate_average_confidence(df)

    common_emotion = get_most_common_emotion(df)

    # =========================================
    # METRIC CARDS
    # =========================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Journals",
            total_entries
        )

    with col2:
        st.metric(
            "Average Confidence",
            avg_confidence
        )

    with col3:
        st.metric(
            "Most Common Emotion",
            common_emotion
        )

    st.write("")

    # =========================================
    # PIE CHART
    # =========================================

    pie_chart = create_emotion_pie_chart(df)

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    # =========================================
    # TIMELINE
    # =========================================

    timeline_chart = create_emotion_timeline(df)

    st.plotly_chart(
        timeline_chart,
        use_container_width=True
    )

    # =========================================
    # AI INSIGHT
    # =========================================

    insight = generate_behavioral_insight(
        common_emotion
    )

    st.info(insight)

    # =========================================
    # DATA TABLE
    # =========================================

    st.subheader("📜 Journal Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )