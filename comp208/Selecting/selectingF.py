from sklearn import feature_selection
import pandas as pd


def percentile(data):
    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    qtansformer = feature_selection.SelectPercentile(feature_selection.chi2, percentile=10)
    x_num = qtansformer.fit_transform(x_num)
    nums = pd.DataFrame(x_num)
    data = pd.concat([nums, x_cat], axis=1)

    return data

def kbest(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    qtansformer = feature_selection.SelectKBest(feature_selection.chi2, k=20)
    x_num = qtansformer.fit_transform(x_num)
    nums = pd.DataFrame(x_num)
    data = pd.concat([nums, x_cat], axis=1)

    return data

def fpr(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    qtansformer = feature_selection.SelectPercentile(feature_selection.chi2, percentile=10)
    x_num = qtansformer.fit_transform(x_num)
    nums = pd.DataFrame(x_num)
    data = pd.concat([nums, x_cat], axis=1)

    return data