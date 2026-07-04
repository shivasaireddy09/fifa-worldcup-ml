import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data():
    df = pd.read_csv("data/final_dataset.csv")

    encoder = LabelEncoder()

    df["home_team"] = encoder.fit_transform(df["home_team"])
    df["away_team"] = encoder.fit_transform(df["away_team"])
    df["tournament"] = encoder.fit_transform(df["tournament"])
    df["city"] = encoder.fit_transform(df["city"])
    df["country"] = encoder.fit_transform(df["country"])
    df["neutral"] = encoder.fit_transform(df["neutral"])
    df["result"] = encoder.fit_transform(df["result"])
    return df
