from PyQt5 import QtCore, QtWidgets
from Dashboard import canvasF as functions

class Ui_Form(object):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(479, 381)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 431, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.kmeans = QtWidgets.QPushButton(self.layoutWidget)
        self.kmeans.setObjectName("kmeans")
        self.verticalLayout.addWidget(self.kmeans)
        self.kmeans.clicked.connect(functions.kmeans)
        self.kmeans.clicked.connect(Form.close)

        self.shift = QtWidgets.QPushButton(self.layoutWidget)
        self.shift.setObjectName("shift")
        self.verticalLayout.addWidget(self.shift)
        self.shift.clicked.connect(functions.shift)
        self.shift.clicked.connect(Form.close)

        self.gmms = QtWidgets.QPushButton(self.layoutWidget)
        self.gmms.setObjectName("gmms")
        self.verticalLayout.addWidget(self.gmms)
        self.gmms.clicked.connect(functions.gussian)
        self.gmms.clicked.connect(Form.close)

        self.dbscan = QtWidgets.QPushButton(self.layoutWidget)
        self.dbscan.setObjectName("dbscan")
        self.verticalLayout.addWidget(self.dbscan)
        self.dbscan.clicked.connect(functions.dbscan)
        self.dbscan.clicked.connect(Form.close)

        self.hc = QtWidgets.QPushButton(self.layoutWidget)
        self.hc.setObjectName("hc")
        self.verticalLayout.addWidget(self.hc)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.hc.clicked.connect(functions.birch)
        self.hc.clicked.connect(Form.close)


        self.retranslateUi(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.kmeans.setText(_translate("Form", "K-means"))
        self.shift.setText(_translate("Form", "Mean-Shift"))
        self.gmms.setText(_translate("Form", "GMMs"))
        self.dbscan.setText(_translate("Form", "DBSCAN"))
        self.hc.setText(_translate("Form", "Hierarchical Clustering"))
