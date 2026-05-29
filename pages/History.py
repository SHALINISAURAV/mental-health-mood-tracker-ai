import streamlit as st
import pandas as pd

from database.crud import fetch_journals


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="History | MoodMind AI",
    page_icon="📜",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("📜 Journal History")

st.write(
    "View your previous journal entries and detected emotions."
)

# =========================================
# FETCH DATA
# =========================================

rows = fetch_journals()

# =========================================
# DISPLAY DATA
# =========================================

if len(rows) == 0:

    st.info("No journal entries found.")

else:

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

    st.dataframe(
        df,
        use_container_width=True
    )