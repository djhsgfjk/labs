from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex
from PyQt5.QtWidgets import QMessageBox
import random as rd


# Шифр XOR. Зашифровка и расшифровка
def encryption(textBin, keyBin):
    newText = ""
    m = len(keyBin)
    for j in range(0, len(textBin), 16):
        c = ""
        for i in range(j, j+16):
            x = textBin[i]
            y = keyBin[i % m]
            res = x ^ y
            c += str(res)
        newText += chr(int(c, 2))
    return newText


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 1003)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputForm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm.setGeometry(QtCore.QRect(40, 240, 461, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputForm.setFont(font)
        self.inputForm.setObjectName("inputForm")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setGeometry(QtCore.QRect(40, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputLabel.setFont(font)
        self.inputLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.inputLabel.setWordWrap(True)
        self.inputLabel.setObjectName("inputLabel")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(40, 470, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.outputLabel.setWordWrap(True)
        self.outputLabel.setObjectName("outputLabel")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(40, 70, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyLabel.setFont(font)
        self.keyLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.keyLabel.setObjectName("keyLabel")
        self.encryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptButton.setGeometry(QtCore.QRect(370, 430, 311, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.encryptButton.setFont(font)
        self.encryptButton.setObjectName("encryptButton")
        self.decryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.decryptButton.setGeometry(QtCore.QRect(370, 710, 311, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.decryptButton.setFont(font)
        self.decryptButton.setObjectName("decryptButton")
        self.programName = QtWidgets.QLabel(self.centralwidget)
        self.programName.setGeometry(QtCore.QRect(440, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programName.setFont(font)
        self.programName.setObjectName("programName")
        self.keyBox = QtWidgets.QLineEdit(self.centralwidget)
        self.keyBox.setGeometry(QtCore.QRect(40, 100, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyBox.setFont(font)
        self.keyBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.keyBox.setObjectName("keyBox")
        self.outputForm = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputForm.setGeometry(QtCore.QRect(530, 240, 461, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputForm.setFont(font)
        self.outputForm.setObjectName("outputForm")
        self.inputForm2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm2.setGeometry(QtCore.QRect(40, 520, 461, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputForm2.setFont(font)
        self.inputForm2.setPlaceholderText("")
        self.inputForm2.setObjectName("inputForm2")
        self.outputLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel_2.setGeometry(QtCore.QRect(530, 190, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel_2.setFont(font)
        self.outputLabel_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.outputLabel_2.setWordWrap(True)
        self.outputLabel_2.setObjectName("outputLabel_2")
        self.keyLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel_2.setGeometry(QtCore.QRect(530, 70, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyLabel_2.setFont(font)
        self.keyLabel_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.keyLabel_2.setObjectName("keyLabel_2")
        self.keyBox_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.keyBox_2.setGeometry(QtCore.QRect(530, 100, 461, 31))
        self.keyBox_2.setObjectName("keyBox_2")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(360, 150, 311, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName("generateButton")
        self.outputLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel_3.setGeometry(QtCore.QRect(530, 470, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel_3.setFont(font)
        self.outputLabel_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.outputLabel_3.setWordWrap(True)
        self.outputLabel_3.setObjectName("outputLabel_3")
        self.outputForm_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputForm_2.setGeometry(QtCore.QRect(530, 520, 461, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputForm_2.setFont(font)
        self.outputForm_2.setObjectName("outputForm_2")

        self.outputForm4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputForm4.setGeometry(QtCore.QRect(40, 800, 461, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputForm4.setFont(font)
        self.outputForm4.setObjectName("outputForm4")

        self.outputLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel_4.setGeometry(QtCore.QRect(530, 750, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel_4.setFont(font)
        self.outputLabel_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.outputLabel_4.setWordWrap(True)
        self.outputLabel_4.setObjectName("outputLabel_4")
        self.outputForm_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputForm_3.setGeometry(QtCore.QRect(530, 800, 461, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputForm_3.setFont(font)
        self.outputForm_3.setObjectName("outputForm_3")
        self.outputLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel_5.setGeometry(QtCore.QRect(40, 750, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel_5.setFont(font)
        self.outputLabel_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.outputLabel_5.setWordWrap(True)
        self.outputLabel_5.setObjectName("outputLabel_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.keyBox.setMaxLength(2147483647)
        reg_ex = QtCore.QRegExp("[a-zA-Zа-яА-ЯёЁ0-9]*")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.keyBox)
        self.keyBox.setValidator(input_validator)

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Ошибка")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._mutex = QMutex()
        self.addFunctions()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гаммирование"))
        self.inputForm.setPlaceholderText(_translate("MainWindow", "Введите текст..."))
        self.inputLabel.setText(_translate("MainWindow", "Исходный текст:"))
        self.outputLabel.setText(_translate("MainWindow", "Зашифрованный текст:"))
        self.keyLabel.setText(_translate("MainWindow", "Ключ:"))
        self.encryptButton.setText(_translate("MainWindow", "Зашифровать"))
        self.decryptButton.setText(_translate("MainWindow", "Расшифровать"))
        self.programName.setText(_translate("MainWindow", "Гаммирование"))
        self.keyBox.setPlaceholderText(_translate("MainWindow", "Введите ключ..."))
        self.outputLabel_2.setText(_translate("MainWindow", "Двоичное представление текста:"))
        self.keyLabel_2.setText(_translate("MainWindow", "Двоичное представление ключа:"))
        self.generateButton.setText(_translate("MainWindow", "Сгенерировать"))
        self.outputLabel_3.setText(_translate("MainWindow", "Двоичное представление зашифрованного текста:"))
        self.outputLabel_4.setText(_translate("MainWindow", "Двоичное представление расшифрованного текста:"))
        self.outputLabel_5.setText(_translate("MainWindow", "Расшифрованный текст:"))

    def addFunctions(self):
        self._mutex.lock()
        self.generateButton.clicked.connect(self.generateKey)
        self.keyBox.textEdited.connect(self.outputBinaryKey)
        self.inputForm.textChanged.connect(self.outputBinaryText)
        self.inputForm2.textChanged.connect(self.outputBinaryText2)
        self.encryptButton.clicked.connect(self.crypt)
        self.decryptButton.clicked.connect(self.decrypt)

    def outputBinaryKey(self):
        key = self.keyBox.text()
        keyBinStr = ''.join(f"{ord(i):016b}" for i in key)
        self.keyBox_2.setText(keyBinStr)

    def outputBinaryText(self):
        text = self.inputForm.toPlainText()
        textBinStr = ''.join(f"{ord(i):016b}" for i in text)
        self.outputForm.setText(textBinStr)

    def outputBinaryText2(self):
        text = self.inputForm2.toPlainText()
        textBinStr = ''.join(f"{ord(i):016b}" for i in text)
        self.outputForm_2.setText(textBinStr)

    def strToBin(self, str):
        return [int(x) for x in ''.join(f"{ord(i):016b}" for i in str)]

    def showError(self, text1, text2):
        self.msg.setText(text1)
        self.msg.setInformativeText(text2)
        self.msg.exec_()

    def generateKey(self):
        n = rd.randint(1, 8)
        k = ['0', '1'] * 8 * n
        rd.shuffle(k)
        self.keyBox.clear()
        self.keyBox_2.setText(''.join(k))

    def crypt(self):
        textBinStr = self.outputForm.toPlainText()
        keyBinStr = self.keyBox_2.toPlainText()
        if (len(textBinStr) <= 0):
            self.showError("Текст не был введен", "Введите текст")
            return
        if (len(keyBinStr) <= 0):
            self.showError("Ключ не был введен", "Введите или сгенерируйте ключ")
            return

        # textBinStr = ''.join(f"{ord(i):016b}" for i in text)
        # self.outputForm.setText(textBinStr)

        textBin = [int(x) for x in textBinStr]
        keyBin = [int(x) for x in keyBinStr]
        newText = encryption(textBin, keyBin)
        #print(newText)
        self.inputForm2.clear()
        self.inputForm2.appendPlainText(newText)

    def decrypt(self):
        textBinStr = self.outputForm_2.toPlainText()
        keyBinStr = self.keyBox_2.toPlainText()
        if (len(textBinStr) <= 0):
            self.showError("Текст не был введен", "Введите текст")
            return
        if (len(keyBinStr) <= 0):
            self.showError("Ключ не был введен", "Введите или сгенерируйте ключ")
            return

        textBin = [int(x) for x in textBinStr]
        keyBin = [int(x) for x in keyBinStr]
        newText = encryption(textBin, keyBin)
        #print(newText)
        self.outputForm4.setText(newText)
        textBinStr = ''.join(f"{ord(i):016b}" for i in newText)
        self.outputForm_3.setText(textBinStr)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
