from database.db import get_connection


def create_tables():
    """
    Create database tables
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS journals (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            text TEXT NOT NULL,

            emotion TEXT NOT NULL,

            confidence REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()

    conn.close()