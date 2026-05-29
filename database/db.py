import sqlite3
import os

# ===============================
# SAFE DATABASE PATH (LOCAL + CLOUD)
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "moodmind.db")


# ===============================
# GET DB CONNECTION
# ===============================

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    return conn