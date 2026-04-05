import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def encode_features(X):
    return pd.get_dummies(X, drop_first=True)