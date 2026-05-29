def get_most_common_emotion(df):

    if df.empty:
        return None

    return df["Emotion"].value_counts().idxmax()