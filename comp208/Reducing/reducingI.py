from PyQt5 import QtCore, QtWidgets
from Dashboard import canvasF as functions

class Ui_Reducing():
    def setupUi(self, Reducing):

        Reducing.setObjectName("Reducing")
        Reducing.resize(375, 273)
        self.widget = QtWidgets.QWidget(Reducing)
        self.widget.setGeometry(QtCore.QRect(20, 30, 141, 211))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(Reducing)
        self.widget1.setGeometry(QtCore.QRect(220, 30, 141, 211))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")



        self.mds = QtWidgets.QPushButton(self.widget)
        self.mds.setObjectName("mds")
        self.verticalLayout.addWidget(self.mds)
        self.mds.clicked.connect(functions.mds)
        self.mds.clicked.connect(Reducing.close)

        self.pca = QtWidgets.QPushButton(self.widget)
        self.pca.setObjectName("pca")
        self.verticalLayout.addWidget(self.pca)
        self.pca.clicked.connect(functions.pca)
        self.pca.clicked.connect(Reducing.close)

        self.sne = QtWidgets.QPushButton(self.widget)
        self.sne.setObjectName("sne")
        self.verticalLayout.addWidget(self.sne)
        self.sne.clicked.connect(functions.sne)
        self.sne.clicked.connect(Reducing.close)

        self.isomap = QtWidgets.QPushButton(self.widget1)
        self.isomap.setObjectName("isomap")
        self.verticalLayout_2.addWidget(self.isomap)
        self.isomap.clicked.connect(functions.isomap)
        self.isomap.clicked.connect(Reducing.close)

        self.lda = QtWidgets.QPushButton(self.widget1)
        self.lda.setObjectName("lda")
        self.verticalLayout_2.addWidget(self.lda)
        self.lda.clicked.connect(functions.lda)
        self.lda.clicked.connect(Reducing.close)

        self.tsne = QtWidgets.QPushButton(self.widget1)
        self.tsne.setObjectName("tsne")
        self.verticalLayout_2.addWidget(self.tsne)
        self.tsne.clicked.connect(functions.tsne)
        self.tsne.clicked.connect(Reducing.close)

        self.retranslateUi(Reducing)

    def retranslateUi(self, Reducing):
        _translate = QtCore.QCoreApplication.translate
        Reducing.setWindowTitle(_translate("Reducing", "Form"))
        self.mds.setText(_translate("Reducing", "MDS"))
        self.pca.setText(_translate("Reducing", "PCA"))
        self.sne.setText(_translate("Reducing", "SNE"))
        self.isomap.setText(_translate("Reducing", "ISOMAP"))
        self.lda.setText(_translate("Reducing", "LDA"))
        self.tsne.setText(_translate("Reducing", "t-SNE"))
