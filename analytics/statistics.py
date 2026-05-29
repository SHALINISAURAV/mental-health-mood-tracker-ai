def calculate_total_entries(df):

    return len(df)


def calculate_average_confidence(df):

    if df.empty:
        return 0

    return round(df["Confidence"].mean(), 2)