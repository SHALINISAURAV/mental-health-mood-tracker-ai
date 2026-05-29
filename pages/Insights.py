import streamlit as st

from memory.memory_engine import (
    get_emotion_memory
)

from memory.pattern_detector import (
    detect_emotional_pattern
)

from memory.behavior_tracker import (
    track_behavior
)

from memory.trigger_analysis import (
    analyze_triggers
)

from database.crud import fetch_journals


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Insights | MoodMind AI",
    page_icon="🧠",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("🧠 Behavioral Insights")

st.write(
    "AI-generated emotional behavior analysis."
)

# =========================================
# LOAD EMOTION MEMORY
# =========================================

emotions = get_emotion_memory()

# =========================================
# PATTERN DETECTION
# =========================================

pattern = detect_emotional_pattern(
    emotions
)

st.subheader("📈 Emotional Pattern")

st.info(pattern)

# =========================================
# BEHAVIOR TRACKING
# =========================================

behavior = track_behavior(
    emotions
)

st.subheader("🧭 Behavioral Tracking")

st.warning(behavior)

# =========================================
# TRIGGER ANALYSIS
# =========================================

rows = fetch_journals()

all_triggers = []

for row in rows:

    journal_text = row[1]

    triggers = analyze_triggers(
        journal_text
    )

    all_triggers.extend(triggers)

# =========================================
# DISPLAY TRIGGERS
# =========================================

st.subheader("⚠️ Emotional Triggers")

if len(all_triggers) == 0:

    st.success(
        "No major emotional triggers detected."
    )

else:

    unique_triggers = list(set(all_triggers))

    for trigger in unique_triggers:

        st.error(trigger)