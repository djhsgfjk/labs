from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 759)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)

        self.inputForm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm.setGeometry(QtCore.QRect(110, 150, 751, 221))
        self.inputForm.setFont(font)
        self.inputForm.setObjectName("inputForm")

        self.outputForm = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputForm.setGeometry(QtCore.QRect(110, 490, 751, 221))
        self.outputForm.setText("")
        self.outputForm.setFont(font)
        self.outputForm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputForm.setObjectName("outputForm")

        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(490, 120, 291, 151))
        # self.label.setText("")
        # self.label.setObjectName("label")

        self.encryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptButton.setGeometry(QtCore.QRect(110, 440, 371, 28))
        self.encryptButton.setFont(font)
        self.encryptButton.setObjectName("encryptButton")

        self.decryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.decryptButton.setGeometry(QtCore.QRect(490, 440, 371, 28))
        self.decryptButton.setFont(font)
        self.decryptButton.setObjectName("decryptButton")

        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setGeometry(QtCore.QRect(50, 150, 51, 21))
        self.inputLabel.setFont(font)
        self.inputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.inputLabel.setObjectName("inputLabel")

        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 490, 81, 21))
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")

        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(50, 390, 51, 16))
        self.keyLabel.setFont(font)
        self.keyLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.keyLabel.setObjectName("keyLabel")

        self.langLabel = QtWidgets.QLabel(self.centralwidget)
        self.langLabel.setGeometry(QtCore.QRect(50, 100, 51, 21))
        self.langLabel.setFont(font)
        self.langLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.langLabel.setObjectName("langLabel")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(110, 90, 261, 41))
        # self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.eng = QtWidgets.QRadioButton(self.groupBox)
        self.eng.setGeometry(QtCore.QRect(10, 10, 121, 20))
        self.eng.setFont(font)
        self.eng.setChecked(True)
        self.eng.setObjectName("eng")

        self.rus = QtWidgets.QRadioButton(self.groupBox)
        self.rus.setGeometry(QtCore.QRect(160, 10, 91, 20))
        self.rus.setFont(font)
        self.rus.setObjectName("rus")

        self.keyBox = QtWidgets.QLineEdit(self.centralwidget)
        self.keyBox.setGeometry(QtCore.QRect(110, 390, 751, 31))
        self.keyBox.setFont(font)
        self.keyBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.keyBox.setObjectName("keyBox")

        self.keyBox.setMaxLength(2147483647)
        reg_ex = QtCore.QRegExp("0|(-?[1-9][0-9]*)")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.keyBox)
        self.keyBox.setValidator(input_validator)

        self.programName = QtWidgets.QLabel(self.centralwidget)
        self.programName.setGeometry(QtCore.QRect(360, 40, 211, 31))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programName.setFont(font)
        self.programName.setObjectName("programName")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._mutex = QMutex()
        self.addFunctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.programName.setText(_translate("MainWindow", "Шифрование Цезаря"))
        self.encryptButton.setText(_translate("MainWindow", "Зашифровать"))
        self.decryptButton.setText(_translate("MainWindow", "Расшифровать"))
        self.inputForm.setPlaceholderText(_translate("MainWindow", "Введите текст..."))
        self.inputLabel.setText(_translate("MainWindow", "Текст:"))
        self.outputLabel.setText(_translate("MainWindow", "Результат:"))
        self.keyBox.setPlaceholderText(_translate("MainWindow", "Введите число..."))
        self.keyLabel.setText(_translate("MainWindow", "Ключ:"))
        self.langLabel.setText(_translate("MainWindow", "Язык:"))
        self.eng.setText(_translate("MainWindow", "Английский"))
        self.rus.setText(_translate("MainWindow", "Русский"))

    def addFunctions(self):
        self._mutex.lock()
        self.encryptButton.clicked.connect(lambda: self.crypt())
        self.decryptButton.clicked.connect(lambda: self.decrypt())


    def get_values(self):
        if self.rus.isChecked():
            alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"
        else:
            alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        original_word = self.inputForm.toPlainText()
        n = int(self.keyBox.text())
        return alph, original_word, n

    def crypt(self):
        alph, original_word, n = self.get_values()
        print(alph, original_word, n)
        if (n > 0 and len(original_word) >0):
            word = list(original_word.upper())
            for i in range(len(word)):
                # номер буквы в алфавите
                try:
                    ind = alph.index(word[i])
                except:
                    word[i] = original_word[i]
                    continue
                if word[i] == original_word[i]:
                    word[i] = alph[(ind + n) % len(alph)]
                else:
                    word[i] = alph[(ind + n) % len(alph)].lower()
            print(''.join(word))
            self.outputForm.setText(''.join(word))


    def decrypt(self):
        alph, original_word, n = self.get_values()
        print(alph, original_word, n)
        if (n > 0 and len(original_word) > 0):
            word = list(original_word.upper())
            for i in range(len(word)):
                # номер буквы в алфавите
                try:
                    ind = alph.index(word[i])
                except:
                    word[i] = original_word[i]
                    continue
                # проверка на то, чтобы буковка не вылезла из алфавита
                if (ind - n >= len(alph)):
                    ind -= len(alph)
                elif (ind - n < 0):
                    ind += len(alph)
                if word[i] == original_word[i]:
                    word[i] = alph[(ind - n) % len(alph)]
                else:
                    word[i] = alph[(ind - n) % len(alph)].lower()
            self.outputForm.setText(''.join(word))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())