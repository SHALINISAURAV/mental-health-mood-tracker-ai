from database.db import get_connection


# =========================================
# SAVE JOURNAL
# =========================================
def save_journal(text, emotion, confidence):
    """
    Save journal entry to database
    """

    conn = get_connection()

    try:
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

    except Exception as e:
        print(f"[DB ERROR] save_journal failed: {e}")

    finally:
        conn.close()


# =========================================
# FETCH JOURNALS
# =========================================
def fetch_journals():
    """
    Fetch all journal entries
    """

    conn = get_connection()

    try:
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
        return rows

    except Exception as e:
        print(f"[DB ERROR] fetch_journals failed: {e}")
        return []

    finally:
        conn.close()