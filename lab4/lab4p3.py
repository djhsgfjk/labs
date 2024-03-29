from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import re
from generateKeys import *
from RSA import *


# https://e-nigma.ru/stat/rsa/


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1405, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(40, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(750, 310, 591, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.programName = QtWidgets.QLabel(self.centralwidget)
        self.programName.setGeometry(QtCore.QRect(370, 20, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programName.setFont(font)
        self.programName.setAlignment(QtCore.Qt.AlignCenter)
        self.programName.setObjectName("programName")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(590, 100, 81, 41))
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
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(40, 280, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label4.setFont(font)
        self.label4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label4.setWordWrap(True)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(590, 360, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label5.setFont(font)
        self.label5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label5.setWordWrap(True)
        self.label5.setObjectName("label5")
        self.p = QtWidgets.QTextBrowser(self.centralwidget)
        self.p.setGeometry(QtCore.QRect(140, 190, 381, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p.setFont(font)
        self.p.setObjectName("p")
        self.q = QtWidgets.QTextBrowser(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(140, 290, 381, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q.setFont(font)
        self.q.setObjectName("q")
        self.inputForm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm.setGeometry(QtCore.QRect(750, 100, 591, 181))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputForm.setFont(font)
        self.inputForm.setObjectName("inputForm")
        self.openFromFile = QtWidgets.QPushButton(self.centralwidget)
        self.openFromFile.setGeometry(QtCore.QRect(590, 150, 151, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.openFromFile.setFont(font)
        self.openFromFile.setObjectName("openFromFile")
        self.phi = QtWidgets.QTextBrowser(self.centralwidget)
        self.phi.setGeometry(QtCore.QRect(140, 490, 381, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phi.setFont(font)
        self.phi.setObjectName("phi")
        self.n = QtWidgets.QTextBrowser(self.centralwidget)
        self.n.setGeometry(QtCore.QRect(140, 390, 381, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.n.setFont(font)
        self.n.setObjectName("n")
        self.label3_2 = QtWidgets.QLabel(self.centralwidget)
        self.label3_2.setGeometry(QtCore.QRect(40, 380, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label3_2.setFont(font)
        self.label3_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label3_2.setWordWrap(True)
        self.label3_2.setObjectName("label3_2")
        self.label4_2 = QtWidgets.QLabel(self.centralwidget)
        self.label4_2.setGeometry(QtCore.QRect(40, 480, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label4_2.setFont(font)
        self.label4_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label4_2.setWordWrap(True)
        self.label4_2.setObjectName("label4_2")
        self.label3_3 = QtWidgets.QLabel(self.centralwidget)
        self.label3_3.setGeometry(QtCore.QRect(40, 590, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label3_3.setFont(font)
        self.label3_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label3_3.setWordWrap(True)
        self.label3_3.setObjectName("label3_3")
        self.d = QtWidgets.QTextBrowser(self.centralwidget)
        self.d.setGeometry(QtCore.QRect(140, 590, 381, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d.setFont(font)
        self.d.setObjectName("d")
        self.e = QtWidgets.QTextBrowser(self.centralwidget)
        self.e.setGeometry(QtCore.QRect(140, 690, 381, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.e.setFont(font)
        self.e.setObjectName("e")
        self.label3_4 = QtWidgets.QLabel(self.centralwidget)
        self.label3_4.setGeometry(QtCore.QRect(40, 690, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label3_4.setFont(font)
        self.label3_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label3_4.setWordWrap(True)
        self.label3_4.setObjectName("label3_4")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(750, 580, 591, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.result2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.result2.setGeometry(QtCore.QRect(750, 640, 591, 181))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.result2.setFont(font)
        self.result2.setObjectName("result2")
        self.label5_2 = QtWidgets.QLabel(self.centralwidget)
        self.label5_2.setGeometry(QtCore.QRect(590, 640, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label5_2.setFont(font)
        self.label5_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label5_2.setWordWrap(True)
        self.label5_2.setObjectName("label5_2")
        self.generateKeys = QtWidgets.QPushButton(self.centralwidget)
        self.generateKeys.setGeometry(QtCore.QRect(40, 790, 481, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.generateKeys.setFont(font)
        self.generateKeys.setObjectName("generateKeys")
        self.inputForm_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm_2.setGeometry(QtCore.QRect(750, 370, 591, 181))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputForm_2.setFont(font)
        self.inputForm_2.setObjectName("inputForm_2")
        self.bits = QtWidgets.QSpinBox(self.centralwidget)
        self.bits.setGeometry(QtCore.QRect(140, 110, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bits.setFont(font)
        self.bits.setMinimum(3)
        self.bits.setMaximum(512)
        self.bits.setObjectName("bits")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA"))
        self.label1.setText(_translate("MainWindow", "Битность:"))
        self.button.setText(_translate("MainWindow", "Зашифровать"))
        self.programName.setText(_translate("MainWindow", "RSA"))
        self.label2.setText(_translate("MainWindow", "Текст:"))
        self.label3.setText(_translate("MainWindow", "p = "))
        self.label4.setText(_translate("MainWindow", "q = "))
        self.label5.setText(_translate("MainWindow", "Зашифрованный текст:"))
        self.inputForm.setPlaceholderText(_translate("MainWindow", "Введите текст..."))
        self.openFromFile.setText(_translate("MainWindow", "Выбрать из файла..."))
        self.label3_2.setText(_translate("MainWindow", "n = "))
        self.label4_2.setText(_translate("MainWindow", "φ(n) ="))
        self.label3_3.setText(_translate("MainWindow", "d = "))
        self.label3_4.setText(_translate("MainWindow", "e = "))
        self.button_2.setText(_translate("MainWindow", "Расшифровать"))
        self.label5_2.setText(_translate("MainWindow", "Расшифрованный текст:"))
        self.generateKeys.setText(_translate("MainWindow", "Сгенерировать ключи"))
        self.inputForm_2.setPlaceholderText(_translate("MainWindow", "Введите текст..."))

    def addFunctions(self):
        self._mutex.lock()
        self.generateKeys.clicked.connect(self.getKeys)
        self.openFromFile.clicked.connect(self.browseFile)
        self.button.clicked.connect(self.crypt)
        self.button_2.clicked.connect(self.decrypt)
        self.inputForm_2.textChanged.connect(self.validate)

    def validate(self):
        text = self.inputForm_2.toPlainText()
        res = re.sub(r'[^01]', "", text)
        if len(res) < len(text):
            self.inputForm_2.clear()
            self.inputForm_2.appendPlainText(res)


    def showError(self, text1, text2=""):
        self.msg.setText(text1)
        self.msg.setInformativeText(text2)
        self.msg.exec_()

    def getTextFromFile(self, file):
        if not file:
            self.showError("Невозможно открыть файл", "")
            return None
        try:
            f = open(file, "r", encoding='utf-8')
        except:
            self.showError("Невозможно открыть файл", "")
            return None
        try:
            text = f.read()
        except:
            self.showError("Невозможно прочитать файл", "")
            f.close()
            return None
        f.close()
        return text

    def browseFile(self):
        files = QFileDialog.getOpenFileName(self.centralwidget, "Выбрать файл", ".", "Text files (*.txt)")
        if len(files[0]) > 0:
            filePath = files[0]
            text = self.getTextFromFile(filePath)
            if not text == None:
                self.inputForm.clear()
                self.inputForm.appendPlainText(text)

    def getKeys(self):
        bits = int(self.bits.text())
        print("bits:", bits)
        p, q, n, phi, e, d = generateKeys(bits)
        self.p.setText(str(p))
        self.q.setText(str(q))
        self.n.setText(str(n))
        self.phi.setText(str(phi))
        self.e.setText(str(e))
        self.d.setText(str(d))

    def crypt(self):
        if len(self.p.toPlainText()) == 0:
            self.getKeys()
        text = self.inputForm.toPlainText()
        if len(text) == 0:
            self.showError("Введите текст")
            return
        e = int(self.e.toPlainText())
        n = int(self.n.toPlainText())
        result = cryptRSA(text, e, n)
        print(result)
        self.inputForm_2.clear()
        self.inputForm_2.appendPlainText(result)

    def decrypt(self):
        if len(self.p.toPlainText()) == 0:
            self.getKeys()
        text = self.inputForm_2.toPlainText()
        if len(text) == 0:
            self.showError("Введите шифротекст")
            return
        d = int(self.d.toPlainText())
        n = int(self.n.toPlainText())
        result = decryptRSA(text, d, n)
        print(result)
        self.result2.setText(result)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
