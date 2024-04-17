import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn.mixture import GaussianMixture
from sklearn.cluster import Birch
from sklearn.cluster import DBSCAN


def kmeans(data):
    x_num = data.select_dtypes(include="number")

    kmeans = KMeans(n_clusters=3).fit(x_num)
    labels = pd.DataFrame(kmeans.labels_)

    #Output datax
    datax = pd.concat([data,labels],axis=1)
    return datax

def MeanShift(data):
    x_num = data.select_dtypes(include="number")

    shift = MeanShift(bandwidth=2).fit(x_num)
    labels = pd.DataFrame(shift.labels_)

    #Output datax
    datax = pd.concat([data,labels],axis=1)
    return datax

def GMMs(data):
    x_num = data.select_dtypes(include="number")

    gm = GaussianMixture().fit(x_num)
    labels = pd.DataFrame(gm.labels_)

    #Output datax
    datax = pd.concat([data,labels],axis=1)
    return datax

def DBSCAN(data):
    x_num = data.select_dtypes(include="number")

    dbscan = DBSCAN().fit(x_num)
    labels = pd.DataFrame(dbscan.labels_)

    #Output datax
    datax = pd.concat([data,labels],axis=1)
    return datax

def BIRCH(data):
    x_num = data.select_dtypes(include="number")

    cluster = Birch().fit(x_num)
    labels = pd.DataFrame(cluster.labels_)

    # Output datax
    datax = pd.concat([data, labels], axis=1)
    return datax

