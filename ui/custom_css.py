CUSTOM_CSS = """
<style>

/* =========================================
GLOBAL APP STYLE
========================================= */

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    color: white;
}

/* =========================================
SCROLLBAR
========================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #8b5cf6;
    border-radius: 10px;
}

/* =========================================
HERO TITLE
========================================= */

.hero-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
    margin-bottom: 0;
}

.hero-subtitle {
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 5px;
}

/* =========================================
GLASS CARD (FEATURES)
========================================= */

.glass-card {
    background: rgba(30, 41, 59, 0.7);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    transition: 0.3s;
}

.glass-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.5);
}

/* =========================================
EMOTION BOX
========================================= */

.emotion-box {
    background: linear-gradient(135deg, #1e293b, #312e81);
    padding: 20px;
    border-radius: 16px;
    border-left: 5px solid #8b5cf6;
    margin-top: 15px;
}

/* =========================================
BUTTON STYLE
========================================= */

.stButton > button {
    background: linear-gradient(135deg, #8b5cf6, #7c3aed);
    color: white;
    font-size: 16px;
    padding: 10px;
    border-radius: 10px;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(139,92,246,0.5);
}

/* =========================================
TEXT AREA
========================================= */

textarea {
    border-radius: 12px !important;
    font-size: 16px !important;
}

/* =========================================
METRICS
========================================= */

[data-testid="metric-container"] {
    background: rgba(30, 41, 59, 0.7);
    padding: 15px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.08);
}

</style>
"""