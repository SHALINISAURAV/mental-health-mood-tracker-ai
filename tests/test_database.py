from database.schema import create_tables

from database.crud import (
    save_journal,
    fetch_journals
)


def test_database_save():

    # Create tables first

    create_tables()

    # Save test journal

    save_journal(
        text="Test journal",
        emotion="joy",
        confidence=0.99
    )

    # Fetch journals

    rows = fetch_journals()

    assert len(rows) > 0