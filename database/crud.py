from database.db import get_connection


# =========================================
# SAVE JOURNAL
# =========================================

def save_journal(text, emotion, confidence):
    """
    Save journal entry to database
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO journals (
            text,
            emotion,
            confidence
        )

        VALUES (?, ?, ?)
        """,
        (text, emotion, confidence)
    )

    conn.commit()

    conn.close()


# =========================================
# FETCH JOURNALS
# =========================================

def fetch_journals():
    """
    Fetch all journal entries
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            text,
            emotion,
            confidence,
            created_at

        FROM journals

        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows