import pandas as pd
from Reducing import reducingF
from Encoding import encodingF
from Clustering import clusteringF
from Cleaning import cleaningF
from Transforming import transformingF
from Selecting import selectingF




data = pd.DataFrame([1, 2, 3])
process = "The workshop is prepared!"


def loadFile(name):
    global data
    data = pd.read_csv(name)


def getHead():
    global data
    return data.head().to_string()


def updateData(temp):
    global data
    data = temp


def saveData(directory):
    global data
    data.to_csv(directory + '/demo.csv')


def processLine(str):
    global process
    process = process + "\nYou have done the " + str + " work!"


def mds():
    global data
    data = reducingF.mds(data)


def sne():
    global data
    data = reducingF.sne(data)
    processLine("Spectral Embedding for 2-dimension")

def isomap():
    global data
    data = reducingF.isomap(data)
    processLine("Isometric Mapping")

def lda():
    global data
    data = reducingF.lda(data)
    processLine("Locally linear embedding")

def tsne():
    global data
    data = reducingF.tsne(data)
    processLine("t-distributed stochastic neighbor embedding for 2-dimension")

def pca():
    global data
    data = reducingF.pca(data)
    processLine("Principle component analysis")

def onehot():
    global data
    data = encodingF.onehot(data)
    processLine("onehot encoding")

def ordinal():
    global data
    data = encodingF.ordinal(data)
    processLine("ordinal encoding")

def label():
    global data
    data = encodingF.label(data)
    processLine("label encoding")

def binary():
    global data
    data = encodingF.binary(data)
    processLine("binary encoding")

def target():
    global data
    data = encodingF.target(data)
    processLine("target encoding")

def frequency():
    global data
    data = encodingF.frequency(data)
    processLine("frequency encoding")

def kmeans():
    global data
    data = clusteringF.kmeans(data)
    processLine("K-means clustering")

def dbscan():
    global data
    data = clusteringF.DBSCAN(data)
    processLine("DBSCAN clustering")

def shift():
    global data
    data = clusteringF.MeanShift(data)
    processLine("Meanshift clustering")

def birch():
    global data
    data = clusteringF.BIRCH(data)
    processLine("Birch clustering")

def gussian():
    global data
    data = clusteringF.GMMs(data)
    processLine("Gaussian mixture modeling")

def dropna():
    global data
    data = cleaningF.dropnas(data)
    processLine("dropna cleaning")


def means():
    global data
    data = cleaningF.means(data)
    processLine("means cleaning")


def medians():
    global data
    data = cleaningF.medians(data)
    processLine("medians cleaning")

def modes():
    global data
    data = cleaningF.modes(data)
    processLine("modes cleaning")


def standards():
    global data
    data = transformingF.standards(data)
    processLine("standards transforming")


def minabs():
    global data
    data = transformingF.minabs(data)
    processLine("minabs transforming")


def minmaxs():
    global data
    data = transformingF.minmaxs(data)
    processLine("minmaxs transforming")


def quantiles():
    global data
    data = transformingF.quantiles(data)
    processLine("quantiles transforming")


def percentile():
    global data
    data = selectingF.percentile(data)
    processLine("percentile selecting")


def kbest():
    global data
    data = selectingF.kbest(data)
    processLine("kbest selecting")


def fpr():
    global data
    data = selectingF.fpr(data)
    processLine("fpr selecting")


