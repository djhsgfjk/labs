from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import numpy as np

rusAlph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789"
engAlph = "abcdefghijklmnopqrstuvwxyz0123456789"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 915)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputForm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm.setGeometry(QtCore.QRect(40, 180, 561, 231))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputForm.setFont(font)
        self.inputForm.setObjectName("inputForm")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setGeometry(QtCore.QRect(40, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputLabel.setFont(font)
        self.inputLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.inputLabel.setWordWrap(True)
        self.inputLabel.setObjectName("inputLabel")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(40, 530, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyLabel.setFont(font)
        self.keyLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.keyLabel.setObjectName("keyLabel")
        self.openFromFile = QtWidgets.QPushButton(self.centralwidget)
        self.openFromFile.setGeometry(QtCore.QRect(310, 430, 291, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.openFromFile.setFont(font)
        self.openFromFile.setObjectName("openFromFile")
        self.decryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.decryptButton.setGeometry(QtCore.QRect(40, 480, 561, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.decryptButton.setFont(font)
        self.decryptButton.setObjectName("decryptButton")
        self.programName = QtWidgets.QLabel(self.centralwidget)
        self.programName.setGeometry(QtCore.QRect(170, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programName.setFont(font)
        self.programName.setObjectName("programName")
        self.langLabel = QtWidgets.QLabel(self.centralwidget)
        self.langLabel.setGeometry(QtCore.QRect(40, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.langLabel.setFont(font)
        self.langLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.langLabel.setObjectName("langLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 90, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.eng = QtWidgets.QRadioButton(self.groupBox)
        self.eng.setEnabled(True)
        self.eng.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.eng.setFont(font)
        self.eng.setChecked(True)
        self.eng.setObjectName("eng")
        self.rus = QtWidgets.QRadioButton(self.groupBox)
        self.rus.setGeometry(QtCore.QRect(150, 10, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.rus.setFont(font)
        self.rus.setObjectName("rus")
        self.outputForm = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputForm.setGeometry(QtCore.QRect(40, 630, 561, 231))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputForm.setFont(font)
        self.outputForm.setObjectName("outputForm")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(40, 590, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.outputLabel.setWordWrap(True)
        self.outputLabel.setObjectName("outputLabel")
        self.inputLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel2.setGeometry(QtCore.QRect(40, 430, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputLabel2.setFont(font)
        self.inputLabel2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.inputLabel2.setWordWrap(True)
        self.inputLabel2.setObjectName("inputLabel2")
        self.keyOutputForm = QtWidgets.QTextBrowser(self.centralwidget)
        self.keyOutputForm.setGeometry(QtCore.QRect(40, 560, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyOutputForm.setFont(font)
        self.keyOutputForm.setObjectName("keyOutputForm")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Взлом шифровния Виженера"))
        self.inputForm.setPlaceholderText(_translate("MainWindow", "Введите текст..."))
        self.inputLabel.setText(_translate("MainWindow", "Текст:"))
        self.keyLabel.setText(_translate("MainWindow", "Ключ:"))
        self.openFromFile.setText(_translate("MainWindow", "Выбрать файл..."))
        self.decryptButton.setText(_translate("MainWindow", "Расшифровать"))
        self.programName.setText(_translate("MainWindow", "Взлом шифрования Виженера"))
        self.langLabel.setText(_translate("MainWindow", "Язык:"))
        self.eng.setText(_translate("MainWindow", "Английский"))
        self.rus.setText(_translate("MainWindow", "Русский"))
        self.outputLabel.setText(_translate("MainWindow", "Результат дешифрования:"))
        self.inputLabel2.setText(_translate("MainWindow", "Расшифровать текст из файла (txt):"))

    def addFunctions(self):
        self._mutex.lock()
        self.openFromFile.clicked.connect(self.browseFile)
        self.decryptButton.clicked.connect(self.decrypt)

    def showError(self, text1, text2):
        self.msg.setText(text1)
        self.msg.setInformativeText(text2)
        self.msg.exec_()

    def getTextFromFile(self, file):
        if not file:
            self.showError("Невозможно открыть файл", "")
            return ""
        try:
            f = open(file, "r", encoding='utf-8')
        except:
            self.showError("Невозможно открыть файл", "")
            return ""
        try:
            text = f.read()
        except:
            self.showError("Невозможно прочитать файл", "")
            f.close()
            return ""
        f.close()
        return text

    def browseFile(self):
        files = QFileDialog.getOpenFileName(self.centralwidget, "Выбрать файл", ".", "Text files (*.txt)")
        if len(files[0]) > 0:
            filePath = files[0]
            # fileName = re.search(r'[~@#$%^-_(){}\'`\d\w]*\.txt\b', filePath).group(0)
            # print(filePath)

            text = self.getTextFromFile(filePath)
            if text:
                self.inputForm.clear()
                self.inputForm.appendPlainText(text)

    def frequencyAnalysis(self, alph, text):
        frequencyDict = dict.fromkeys(list(alph), 0)
        for letter in text:
            if letter in alph:
                frequencyDict[letter] += 1
        n = len(text)
        for key in frequencyDict:
            frequencyDict[key] = round(frequencyDict[key] / n, 4)
        return frequencyDict

    def maxValueKey(self, d: dict):
        maxV = list(d.values())[0]
        maxK = 0
        for key in d:
            if d[key] > maxV:
                maxV = d[key]
                maxK = key
        print(maxK)
        return maxK

    def findKey(self, alph, frequencyDict, textDict):
        l1 = self.maxValueKey(textDict)
        l2 = self.maxValueKey(frequencyDict)
        return alph.index(l1) - alph.index(l2) % len(alph)


    def decryptText(self, alph, key, text):
        newText = list(text.lower())
        n = len(text)
        m = len(key)
        l = len(alph)
        j = 0
        for i in range(n):
            try:
                ind = alph.index(newText[i])
            except:
                continue
            step = alph.index(key[j % m])
            j += 1
            if newText[i] == text[i]:
                newText[i] = alph[(ind - step) % l]
            else:
                newText[i] = alph[(ind - step) % l].upper()
        return ''.join(newText)


    def getKeyLen(self, alph, text):
        pass


    def decrypt(self):
        text = self.inputForm.toPlainText().lower()
        n = len(text)
        if n <= 0:
            self.showError("Текст не был введен", "Введите текст")
            return

        if self.rus.isChecked():
            alph = rusAlph
            testText = self.getTextFromFile("rus.txt").lower()
        else:
            alph = engAlph
            testText = self.getTextFromFile("eng.txt").lower()

        if len(testText) <= 0:
            self.showError("Ошибка при чтении файла для составления частотных статистик", "")
            return

        frequencyDict = self.frequencyAnalysis(alph, testText)
        print(frequencyDict)

        keyLen = self.getKeyLen(alph, text)
        print(keyLen)
        arr = []
        i = 0
        while i < n:
            print(i)
            j = 0
            while j < keyLen and i < n:
                s = text[i].lower()
                if s in alph:
                    arr.append(s)
                    j += 1
                i += 1
        while j < keyLen:
            print("j =", j)
            arr.append(' ')
            j += 1

        m = len(arr)
        print(m)
        arr = np.array(arr)
        arr.shape = (m // keyLen, keyLen)
        print(arr)

        key = ""
        for i in range(keyLen):
            print(list(arr[:, i]))
            textDict = self.frequencyAnalysis(alph, list(arr[:, i]))
            print(textDict)
            keyPart = self.findKey(alph, frequencyDict, textDict)
            key += alph[keyPart]

        print(key)

        decrypyedText = self.decryptText(alph, key, text)

        self.keyOutputForm.setText(key)
        self.outputForm.setText(decrypyedText)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
