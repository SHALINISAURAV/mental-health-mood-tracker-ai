CUSTOM_CSS = """
<style>

/* =========================================
MAIN APP
========================================= */

.stApp {
    background-color: #0f172a;
    color: white;
}

/* =========================================
SCROLLBAR
========================================= */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: #8b5cf6;
    border-radius: 10px;
}

/* =========================================
HEADINGS
========================================= */

.hero-title {
    font-size: 60px;
    font-weight: 800;
    color: white;
    margin-bottom: 0;
}

.hero-subtitle {
    font-size: 24px;
    color: #cbd5e1;
}

/* =========================================
GLASS CARD
========================================= */

.glass-card {

    background: rgba(30, 41, 59, 0.7);

    padding: 25px;

    border-radius: 20px;

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.1);

    box-shadow: 0 8px 32px rgba(0,0,0,0.3);

    transition: 0.3s;
}

.glass-card:hover {

    transform: translateY(-8px);

    box-shadow: 0 12px 40px rgba(0,0,0,0.5);
}

/* =========================================
EMOTION BOX
========================================= */

.emotion-box {

    background: linear-gradient(
        135deg,
        #1e293b,
        #312e81
    );

    padding: 25px;

    border-radius: 20px;

    border-left: 6px solid #8b5cf6;

    margin-top: 20px;
}

/* =========================================
BUTTONS
========================================= */

.stButton > button {

    width: 100%;

    height: 3em;

    border-radius: 12px;

    background: linear-gradient(
        135deg,
        #8b5cf6,
        #7c3aed
    );

    color: white;

    font-size: 18px;

    font-weight: bold;

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

    font-size: 18px !important;

    border-radius: 15px !important;
}

/* =========================================
METRIC CARDS
========================================= */

[data-testid="metric-container"] {

    background: rgba(30, 41, 59, 0.7);

    border-radius: 20px;

    padding: 15px;

    border: 1px solid rgba(255,255,255,0.08);
}

</style>
"""