from database.crud import fetch_journals


def get_emotion_memory():

    rows = fetch_journals()

    emotions = []

    for row in rows:

        emotions.append(row[2])

    return emotions