import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import KBinsDiscretizer


def onehot(data):
    # Separate categorical and numerical features
    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    # One-hot encode categorical features
    encoder = OneHotEncoder()
    encoded_cat = encoder.fit_transform(x_cat)
    encoded_cat_df = pd.DataFrame(encoded_cat.toarray(),
                                  columns=encoder.get_feature_names_out(x_cat.columns.astype(str)))

    # Concatenate encoded categorical features with numerical features
    data_encoded = pd.concat([x_num, encoded_cat_df], axis=1)


    return data_encoded

def binary(data):
    # Separate categorical and numerical features
    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    # Binary encode categorical features
    binary_encoded = pd.get_dummies(x_cat, drop_first=True)

    # Align index of numerical features with binary encoded features
    x_num_reset = x_num.reset_index(drop=True)
    binary_encoded_reset = binary_encoded.reset_index(drop=True)

    # Concatenate numerical features with binary encoded categorical features
    data_encoded = pd.concat([x_num_reset, binary_encoded_reset], axis=1)

    return data_encoded


def target(data):
    # Separate categorical and numerical features
    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    # Find target variable
    target_variable = data.columns.difference(x_cat.columns)[0]

    for col in x_cat.columns:
        mean_encoding = data.groupby(col)[target_variable].mean()
        # 获取目标变量均值为1的类别
        high_mean_categories = mean_encoding[mean_encoding == 1].index
        # 将除了目标变量均值为1的类别外的类别编码为0，目标变量均值为1的类别编码为1
        data[col] = data[col].apply(lambda x: 1 if x in high_mean_categories else 0)

    return data


def label(data):
    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    for col in x_cat.columns:
        label_encoder = LabelEncoder()
        data[col] = label_encoder.fit_transform(data[col])

    data_encoded = pd.concat([x_num, data[x_cat.columns]], axis=1)

    return data_encoded

def ordinal(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    orde = OrdinalEncoder(dtype=np.int32, handle_unknown='use_encoded_value', unknown_value=-1)
    for col in discrete_cols:
        col_name = 'OrdinalEncoder_' + col
        orde.fit(df_combine[col].values.reshape(-1, 1))
        df_train[col_name] = orde.transform(df_train[col].values.reshape(-1, 1))
        df_test[col_name] = orde.transform(df_test[col].values.reshape(-1, 1))

    return data


def frequency(data):
    # Separate categorical and numerical features
    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    # Perform frequency encoding for each categorical column
    for col in x_cat.columns:
        freq_encoding = data[col].value_counts(normalize=True).to_dict()
        data[col] = data[col].map(freq_encoding).round().astype(int)


    return data
