import streamlit as st


def render_dashboard_metrics(
    total_entries,
    top_emotion
):

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            label="📝 Total Journals",
            value=total_entries
        )

    with col2:

        st.metric(
            label="🎯 Top Emotion",
            value=top_emotion
        )