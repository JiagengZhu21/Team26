from PyQt5 import QtCore, QtWidgets
from Dashboard import canvasF as functions

class Ui_cleaning(object):

    def setupUi(self, cleaning):

        cleaning.setObjectName("cleaning")
        cleaning.resize(363, 199)

        self.dropna = QtWidgets.QPushButton(cleaning)
        self.dropna.setGeometry(QtCore.QRect(30, 50, 121, 41))
        self.dropna.setObjectName("dropna")
        self.dropna.clicked.connect(functions.dropna)
        self.dropna.clicked.connect(cleaning.close)

        self.mean = QtWidgets.QPushButton(cleaning)
        self.mean.setGeometry(QtCore.QRect(210, 50, 121, 41))
        self.mean.setObjectName("mean")
        self.mean.clicked.connect(functions.means)
        self.mean.clicked.connect(cleaning.close)

        self.median = QtWidgets.QPushButton(cleaning)
        self.median.setGeometry(QtCore.QRect(30, 120, 121, 41))
        self.median.setObjectName("median")
        self.median.clicked.connect(functions.medians)
        self.median.clicked.connect(cleaning.close)

        self.mode = QtWidgets.QPushButton(cleaning)
        self.mode.setGeometry(QtCore.QRect(210, 120, 121, 41))
        self.mode.setObjectName("mode")
        self.mode.clicked.connect(functions.modes)
        self.mode.clicked.connect(cleaning.close)

        self.retranslateUi(cleaning)

    def retranslateUi(self, cleaning):
        _translate = QtCore.QCoreApplication.translate
        cleaning.setWindowTitle(_translate("cleaning", "Form"))
        self.dropna.setText(_translate("cleaning", "Drop"))
        self.mean.setText(_translate("cleaning", "Mean"))
        self.median.setText(_translate("cleaning", "Median"))
        self.mode.setText(_translate("cleaning", "Mode"))
