import sqlite3

from config import DATABASE_PATH


def get_connection():
    """
    Create SQLite database connection
    """

    conn = sqlite3.connect(DATABASE_PATH)

    return conn