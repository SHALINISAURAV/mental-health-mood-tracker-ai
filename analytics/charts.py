import pandas as pd
import plotly.express as px


# =========================================
# EMOTION DISTRIBUTION PIE CHART
# =========================================

def create_emotion_pie_chart(df):

    emotion_counts = (
        df["Emotion"]
        .value_counts()
        .reset_index()
    )

    emotion_counts.columns = [
        "Emotion",
        "Count"
    ]

    fig = px.pie(
        emotion_counts,
        names="Emotion",
        values="Count",
        title="Emotion Distribution"
    )

    return fig


# =========================================
# EMOTION TIMELINE
# =========================================

def create_emotion_timeline(df):

    fig = px.line(
        df,
        x="Created At",
        y="Confidence",
        color="Emotion",
        title="Emotion Timeline"
    )

    return fig