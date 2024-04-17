from PyQt5 import QtCore, QtGui, QtWidgets
from Dashboard import canvasF as functions
from Reducing import reducingI
from Encoding import encodingI
from Clustering import clusteringI
from Cleaning import cleaningI
from Selecting import selectingI
from Transforming import transformingI


class Ui_Main(object):

    def setupUi(self, Main):

        #main widget setup
        Main.setObjectName("Main")
        Main.resize(701, 550)

        #main operators of canvas setup
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 101))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap('images\juju.png'))

        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 151, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(QtGui.QPixmap('images\\xbibi.png'))

        self.file = QtWidgets.QPushButton(Main)
        self.file.setGeometry(QtCore.QRect(340, 10, 131, 51))
        self.file.setObjectName("file")
        self.file.clicked.connect(self.readFile)
        self.file.clicked.connect(self.printHead)

        self.exporter = QtWidgets.QPushButton(Main)
        self.exporter.setGeometry(QtCore.QRect(570, 220, 121, 61))
        self.exporter.setObjectName("exporter")
        self.exporter.clicked.connect(self.exportFile)

        self.transforming = QtWidgets.QPushButton(Main)
        self.transforming.setGeometry(QtCore.QRect(340, 70, 131, 51))
        self.transforming.setObjectName("transforming")
        self.transforming.clicked.connect(self.transformingW)

        self.encoding = QtWidgets.QPushButton(Main)
        self.encoding.setGeometry(QtCore.QRect(180, 70, 131, 51))
        self.encoding.setObjectName("encoding")
        self.encoding.clicked.connect(self.encodingW)

        self.cleaning = QtWidgets.QPushButton(Main)
        self.cleaning.setGeometry(QtCore.QRect(500, 70, 131, 51))
        self.cleaning.setObjectName("cleaning")
        self.cleaning.clicked.connect(self.cleaningW)

        self.clustering = QtWidgets.QPushButton(Main)
        self.clustering.setGeometry(QtCore.QRect(340, 130, 131, 51))
        self.clustering.setObjectName("clustering")
        self.clustering.clicked.connect(self.clusteringW)

        self.selecting = QtWidgets.QPushButton(Main)
        self.selecting.setGeometry(QtCore.QRect(180, 130, 131, 51))
        self.selecting.setObjectName("selecting")
        self.selecting.clicked.connect(self.selectingW)

        self.reducing = QtWidgets.QPushButton(Main)
        self.reducing.setGeometry(QtCore.QRect(500, 130, 131, 51))
        self.reducing.setObjectName("reducing")
        self.reducing.clicked.connect(self.reducingW)

        self.textBrowser = QtWidgets.QTextBrowser(Main)
        self.textBrowser.setGeometry(QtCore.QRect(10, 291, 681, 251))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton = QtWidgets.QPushButton(Main)
        self.pushButton.setGeometry(QtCore.QRect(330, 240, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.refresh)


        #some extra operations
        self.retranslateUi(Main)

    def retranslateUi(self, Main):

        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.file.setText(_translate("Main", "File"))
        self.exporter.setText(_translate("Main", "Export"))
        self.encoding.setText(_translate("Main", "Encoding"))
        self.transforming.setText(_translate("Main", "Transforming"))
        self.cleaning.setText(_translate("Main", "Cleaning"))
        self.selecting.setText(_translate("Main", "Selecting"))
        self.clustering.setText(_translate("Main", "Clustering"))
        self.reducing.setText(_translate("Main", "Reducing"))


    def readFile(self):

        fname, ftype = QtWidgets.QFileDialog.getOpenFileName(None, "Open File",
                         "./", "All Files(*);;Wav(*.wav);;Txt (*.txt)")
        functions.loadFile(fname)

    def printHead(self):

        temp = functions.getHead()
        self.textBrowser.clear()
        self.textBrowser.append(temp)

    def exportFile(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory", "./")
        functions.saveData(directory)

    def reducingW(self):

        self.reducingWin = QtWidgets.QWidget()
        reducing = reducingI.Ui_Reducing()
        reducing.setupUi(self.reducingWin)
        self.reducingWin.show()

    def encodingW(self):

        self.encodingWin = QtWidgets.QWidget()
        encoding = encodingI.Ui_encoding()
        encoding.setupUi(self.encodingWin)
        self.encodingWin.show()

    def clusteringW(self):

        self.clusteringWin = QtWidgets.QWidget()
        clustering = clusteringI.Ui_Form()
        clustering.setupUi(self.clusteringWin)
        self.clusteringWin.show()

    def cleaningW(self):

        self.cleaningWin = QtWidgets.QWidget()
        cleaning = cleaningI.Ui_cleaning()
        cleaning.setupUi(self.cleaningWin)
        self.cleaningWin.show()

    def selectingW(self):

        self.selectingWin = QtWidgets.QWidget()
        selecting = selectingI.Ui_selecting()
        selecting.setupUi(self.selectingWin)
        self.selectingWin.show()

    def transformingW(self):

        self.transformingWin = QtWidgets.QWidget()
        transforming = transformingI.Ui_transforming()
        transforming.setupUi(self.transformingWin)
        self.transformingWin.show()

    def refresh(self):

        self.printHead()
        self.textBrowser.append(functions.process)


def window():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    from qt_material import apply_stylesheet
    apply_stylesheet(app, theme='dark_teal.xml')
    Main.show()
    sys.exit(app.exec_())