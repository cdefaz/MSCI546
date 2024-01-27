import pandas as pd

def load_simple(file: str):
    df = pd.read_csv(file)
    label = df['label'].copy()
    df[df < 85] = -1
    df[(df >= 85) & (df <= 170)] = 0
    df[df > 170] = 1
    df['label'] = label
    return df