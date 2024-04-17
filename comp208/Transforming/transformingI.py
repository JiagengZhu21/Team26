from PyQt5 import QtCore, QtWidgets
from Dashboard import canvasF as functions

class Ui_transforming(object):
    def setupUi(self, transforming):

        transforming.setObjectName("transforming")
        transforming.resize(430, 244)

        self.standard = QtWidgets.QPushButton(transforming)
        self.standard.setGeometry(QtCore.QRect(30, 20, 161, 71))
        self.standard.setObjectName("standard")
        self.standard.clicked.connect(functions.standards)
        self.standard.clicked.connect(transforming.close)

        self.minabs = QtWidgets.QPushButton(transforming)
        self.minabs.setGeometry(QtCore.QRect(240, 20, 171, 71))
        self.minabs.setObjectName("minabs")
        self.minabs.clicked.connect(functions.minabs)
        self.minabs.clicked.connect(transforming.close)

        self.minmax = QtWidgets.QPushButton(transforming)
        self.minmax.setGeometry(QtCore.QRect(30, 150, 161, 71))
        self.minmax.setObjectName("minmax")
        self.minmax.clicked.connect(functions.minmaxs)
        self.minmax.clicked.connect(transforming.close)

        self.quantile = QtWidgets.QPushButton(transforming)
        self.quantile.setGeometry(QtCore.QRect(240, 150, 171, 71))
        self.quantile.setObjectName("quantile")
        self.quantile.clicked.connect(functions.quantiles)
        self.quantile.clicked.connect(transforming.close)

        self.retranslateUi(transforming)

    def retranslateUi(self, transforming):
        _translate = QtCore.QCoreApplication.translate
        transforming.setWindowTitle(_translate("transforming", "Form"))
        self.standard.setText(_translate("transforming", "Standardization"))
        self.minabs.setText(_translate("transforming", "MinAbs"))
        self.minmax.setText(_translate("transforming", "MinMax"))
        self.quantile.setText(_translate("transforming", "Quantile"))
