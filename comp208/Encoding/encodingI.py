from PyQt5 import QtCore, QtWidgets
from Dashboard import canvasF as functions

class Ui_encoding():

    def setupUi(self, encoding):

        encoding.setObjectName("encoding")
        encoding.resize(375, 273)

        self.onehot = QtWidgets.QPushButton(encoding)
        self.onehot.setGeometry(QtCore.QRect(30, 40, 121, 41))
        self.onehot.setObjectName("onehot")
        self.onehot.clicked.connect(functions.onehot)
        self.onehot.clicked.connect(encoding.close)

        self.label = QtWidgets.QPushButton(encoding)
        self.label.setGeometry(QtCore.QRect(210, 40, 121, 41))
        self.label.setObjectName("label")
        self.label.clicked.connect(functions.label)
        self.label.clicked.connect(encoding.close)

        self.ordinal = QtWidgets.QPushButton(encoding)
        self.ordinal.setGeometry(QtCore.QRect(30, 110, 121, 41))
        self.ordinal.setObjectName("ordinal")
        self.ordinal.clicked.connect(functions.ordinal)
        self.ordinal.clicked.connect(encoding.close)

        self.binary = QtWidgets.QPushButton(encoding)
        self.binary.setGeometry(QtCore.QRect(210, 110, 121, 41))
        self.binary.setObjectName("binary")
        self.binary.clicked.connect(functions.binary)
        self.binary.clicked.connect(encoding.close)

        self.target = QtWidgets.QPushButton(encoding)
        self.target.setGeometry(QtCore.QRect(30, 180, 121, 41))
        self.target.setObjectName("target")
        self.target.clicked.connect(functions.target)
        self.target.clicked.connect(encoding.close)

        self.frequency = QtWidgets.QPushButton(encoding)
        self.frequency.setGeometry(QtCore.QRect(210, 180, 121, 41))
        self.frequency.setObjectName("frequency")
        self.frequency.clicked.connect(functions.frequency)
        self.frequency.clicked.connect(encoding.close)

        self.retranslateUi(encoding)

    def retranslateUi(self, encoding):
        _translate = QtCore.QCoreApplication.translate
        encoding.setWindowTitle(_translate("encoding", "Form"))
        self.onehot.setText(_translate("encoding", "One-Hot"))
        self.label.setText(_translate("encoding", "Label"))
        self.ordinal.setText(_translate("encoding", "Ordinal"))
        self.binary.setText(_translate("encoding", "Binary"))
        self.target.setText(_translate("encoding", "Target"))
        self.frequency.setText(_translate("encoding", "Frequency"))
