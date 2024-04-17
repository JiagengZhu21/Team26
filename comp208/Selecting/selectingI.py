from PyQt5 import QtCore, QtWidgets
from Dashboard import canvasF as functions

class Ui_selecting(object):
    def setupUi(self, selecting):

        selecting.setObjectName("selecting")
        selecting.resize(225, 279)

        self.percentile = QtWidgets.QPushButton(selecting)
        self.percentile.setGeometry(QtCore.QRect(40, 10, 161, 71))
        self.percentile.setObjectName("percentile")
        self.percentile.clicked.connect(functions.percentile)
        self.percentile.clicked.connect(selecting.close)

        self.kbest = QtWidgets.QPushButton(selecting)
        self.kbest.setGeometry(QtCore.QRect(40, 190, 161, 71))
        self.kbest.setObjectName("kbest")
        self.kbest.clicked.connect(functions.kbest)
        self.kbest.clicked.connect(selecting.close)

        self.fpr = QtWidgets.QPushButton(selecting)
        self.fpr.setGeometry(QtCore.QRect(40, 100, 161, 71))
        self.fpr.setObjectName("fpr")
        self.fpr.clicked.connect(functions.fpr)
        self.fpr.clicked.connect(selecting.close)

        self.retranslateUi(selecting)

    def retranslateUi(self, selecting):
        _translate = QtCore.QCoreApplication.translate
        selecting.setWindowTitle(_translate("selecting", "Form"))
        self.percentile.setText(_translate("selecting", "Percentile"))
        self.kbest.setText(_translate("selecting", "KBest"))
        self.fpr.setText(_translate("selecting", "Fpr"))
