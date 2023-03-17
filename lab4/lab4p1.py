from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex
from PyQt5.QtWidgets import QMessageBox
from fastModularExponentiation import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(40, 80, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(40, 350, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label4.setFont(font)
        self.label4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label4.setObjectName("label4")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(40, 270, 501, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.programName = QtWidgets.QLabel(self.centralwidget)
        self.programName.setGeometry(QtCore.QRect(70, 20, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programName.setFont(font)
        self.programName.setObjectName("programName")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(160, 340, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(40, 130, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label2.setWordWrap(True)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(40, 180, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label3.setWordWrap(True)
        self.label3.setObjectName("label3")

        self.lineEditC = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditC.setGeometry(QtCore.QRect(160, 190, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditC.setFont(font)
        self.lineEditC.setObjectName("lineEditC")
        self.lineEditB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditB.setGeometry(QtCore.QRect(160, 140, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditB.setFont(font)
        self.lineEditB.setObjectName("lineEditB")
        self.lineEditA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditA.setGeometry(QtCore.QRect(160, 90, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditA.setFont(font)
        self.lineEditA.setObjectName("lineEditA")

        self.lineEditA.setMaxLength(2147483647)
        self.lineEditB.setMaxLength(2147483647)
        self.lineEditC.setMaxLength(2147483647)
        reg_ex = QtCore.QRegExp("0|(-?[1-9][0-9]*)")
        self.lineEditA.setValidator(QtGui.QRegExpValidator(reg_ex, self.lineEditA))
        self.lineEditB.setValidator(QtGui.QRegExpValidator(reg_ex, self.lineEditB))
        self.lineEditC.setValidator(QtGui.QRegExpValidator(reg_ex, self.lineEditC))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Ошибка")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._mutex = QMutex()
        self.addFunctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Быстрое возведение в степень по модулю"))
        self.label1.setText(_translate("MainWindow", "A = "))
        self.label4.setText(_translate("MainWindow", "A^B mod C ="))
        self.button.setText(_translate("MainWindow", "Рассчитать"))
        self.programName.setText(_translate("MainWindow", "Быстрое возведение в степень по модулю"))
        self.label2.setText(_translate("MainWindow", "B = "))
        self.label3.setText(_translate("MainWindow", "C = "))

    def addFunctions(self):
        self._mutex.lock()
        self.button.clicked.connect(self.fastModularExponentiation)

    def showError(self, text1, text2=""):
        self.msg.setText(text1)
        self.msg.setInformativeText(text2)
        self.msg.exec_()

    def fastModularExponentiation(self):
        # checking that editLines are not empty
        A = self.lineEditA.text()
        B = self.lineEditB.text()
        C = self.lineEditC.text()
        if len(A) == 0 or len(B) == 0 or len(C) == 0:
            self.showError("Введите параметры")
            return

        A, B, C = int(A), int(B), int(C)
        result = fastModularExponentiation(A, B, C)
        self.result.setText(str(result))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
