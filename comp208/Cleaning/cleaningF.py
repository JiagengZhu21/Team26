import pandas as pd
import random

def dropnas(data):

    df = pd.DataFrame(data)
    df = df.dropna()
    return df

def means(data):

    data.fillna(random.uniform(1,10), inplace=True)
    return data

def medians(data):

    data.fillna(random.gauss(1, 1), inplace=True)
    return data

def modes(data):

    data.fillna(random.gauss(1, 1), inplace=True)
    return data

