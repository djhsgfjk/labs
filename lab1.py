from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex
import traceback


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputForm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm.setGeometry(QtCore.QRect(110, 150, 751, 221))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputForm.setFont(font)
        self.inputForm.setObjectName("inputForm")
        self.outputForm = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputForm.setGeometry(QtCore.QRect(110, 490, 751, 221))
        #self.outputForm.setText("")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputForm.setFont(font)
        self.outputForm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputForm.setObjectName("outputForm")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setGeometry(QtCore.QRect(50, 150, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputLabel.setFont(font)
        self.inputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.inputLabel.setObjectName("inputLabel")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 490, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(50, 390, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyLabel.setFont(font)
        self.keyLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.keyLabel.setObjectName("keyLabel")
        self.encryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptButton.setGeometry(QtCore.QRect(110, 440, 371, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.encryptButton.setFont(font)
        self.encryptButton.setObjectName("encryptButton")
        self.decryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.decryptButton.setGeometry(QtCore.QRect(490, 440, 371, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.decryptButton.setFont(font)
        self.decryptButton.setObjectName("decryptButton")
        self.programName = QtWidgets.QLabel(self.centralwidget)
        self.programName.setGeometry(QtCore.QRect(360, 40, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programName.setFont(font)
        self.programName.setObjectName("programName")
        self.keyBox = QtWidgets.QLineEdit(self.centralwidget)
        self.keyBox.setGeometry(QtCore.QRect(110, 390, 751, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyBox.setFont(font)
        self.keyBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.keyBox.setObjectName("keyBox")
        self.langLabel = QtWidgets.QLabel(self.centralwidget)
        self.langLabel.setGeometry(QtCore.QRect(50, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.langLabel.setFont(font)
        self.langLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.langLabel.setObjectName("langLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(110, 90, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.eng = QtWidgets.QRadioButton(self.groupBox)
        self.eng.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.eng.setFont(font)
        self.eng.setObjectName("eng")
        self.eng.setChecked(True)
        self.rus = QtWidgets.QRadioButton(self.groupBox)
        self.rus.setGeometry(QtCore.QRect(160, 10, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.rus.setFont(font)
        self.rus.setObjectName("rus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.keyBox.setMaxLength(2147483647)
        reg_ex = QtCore.QRegExp("0|(-?[1-9][0-9]*)")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.keyBox)
        self.keyBox.setValidator(input_validator)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._mutex = QMutex()
        self.addFunctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифровние Цезаря"))
        self.inputForm.setPlaceholderText(_translate("MainWindow", "Введите текст..."))
        self.inputLabel.setText(_translate("MainWindow", "Текст:"))
        self.outputLabel.setText(_translate("MainWindow", "Результат:"))
        self.keyLabel.setText(_translate("MainWindow", "Ключ:"))
        self.encryptButton.setText(_translate("MainWindow", "Зашифровать"))
        self.decryptButton.setText(_translate("MainWindow", "Расшифровать"))
        self.programName.setText(_translate("MainWindow", "Шифрование Цезаря"))
        self.keyBox.setPlaceholderText(_translate("MainWindow", "Введите число..."))
        self.langLabel.setText(_translate("MainWindow", "Язык:"))
        self.eng.setText(_translate("MainWindow", "Английский"))
        self.rus.setText(_translate("MainWindow", "Русский"))


    def addFunctions(self):
        self._mutex.lock()
        self.encryptButton.clicked.connect(lambda: self.crypt())
        self.encryptButton.clicked.connect(lambda: self.decrypt())


    def get_values(self):
        if self.rus.isChecked():
            alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"
        else:
            alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        original_word = self.inputForm.toPlainText()
        n = int(self.keyBox.text())
        return alph, original_word, n

    def crypt(self):
        if (len(self.keyBox.text()) > 0):
            print("start")
            alph, original_word, n = self.get_values()
            word = list(original_word.upper())
            for i in range(len(word)):
                # номер буквы в алфавите
                try:
                    ind = alph.index(word[i])
                except:
                    continue
                if word[i] == original_word[i]:
                    word[i] = alph[(ind + n) % len(alph)]
                else:
                    word[i] = alph[(ind + n) % len(alph)].lower()
            print(''.join(word))
            self.outputForm.setText(''.join(word))


    def decrypt(self):
        if (len(self.keyBox.text()) > 0):
            alph, original_word, n = self.get_values(self)
            word = list(original_word.upper())
            for i in range(len(word)):
                # номер буквы в алфавите
                try:
                    ind = alph.index(word[i])
                except:
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