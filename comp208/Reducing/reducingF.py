import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from sklearn.manifold import Isomap
from sklearn.manifold import TSNE
from sklearn.manifold import SpectralEmbedding as SNE
from sklearn.manifold import LocallyLinearEmbedding as LLE


def mds(data):

    number = int(data.shape[1]/3)
    model = MDS(n_components=number)

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    output = model.fit_transform(x_num)
    nums = pd.DataFrame(output)

    data = pd.concat([nums, x_cat], axis=1)
    return data


def pca(data):

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    model = PCA(n_components=0.98)
    output = model.fit_transform(x_num)
    nums = pd.DataFrame(output)

    data = pd.concat([nums, x_cat], axis=1)
    return data


def sne(data):

    model = SNE(n_components=2)

    x_num = data.select_dtypes(include="number")

    output = model.fit_transform(x_num)
    data = pd.DataFrame(output)

    return data


def isomap(data):

    number = int(data.shape[1] / 3)
    model = Isomap(n_components=number)

    x_cat = data.select_dtypes(include="object")
    x_num = data.select_dtypes(include="number")

    output = model.fit_transform(x_num)
    nums = pd.DataFrame(output)

    data = pd.concat([nums, x_cat], axis=1)

    return data


def lda(data):

    model = LLE(n_components=2)

    x_num = data.select_dtypes(include="number")

    output = model.fit_transform(x_num)
    data = pd.DataFrame(output)

    return data


def tsne(data):

    model = TSNE(n_components=2)

    x_num = data.select_dtypes(include="number")

    output = model.fit_transform(x_num)
    data = pd.DataFrame(output)

    return data

