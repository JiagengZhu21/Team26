from sklearn import preprocessing
import pandas as pd


def standards(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    x_num = preprocessing.scale(x_num)
    nums = pd.DataFrame(x_num)
    data = pd.concat([nums, x_cat], axis=1)

    return data

def minabs(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    min_abs_scaler = preprocessing.MinMaxScaler()
    x_num = min_abs_scaler.fit_transform(x_num)
    nums = pd.DataFrame(x_num)
    data = pd.concat([nums, x_cat], axis=1)

    return data

def minmaxs(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    min_max_scaler = preprocessing.MinMaxScaler()
    x_num = min_max_scaler.fit_transform(x_num)
    nums = pd.DataFrame(x_num)
    data = pd.concat([nums, x_cat], axis=1)

    return data

def quantiles(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    qtansformer = preprocessing.QuantileTransformer()
    x_num = qtansformer.fit_transform(x_num)
    nums = pd.DataFrame(x_num)
    data = pd.concat([nums, x_cat], axis=1)

    return data

