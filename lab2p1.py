from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1284, 807)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inputForm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm.setGeometry(QtCore.QRect(40, 240, 381, 461))
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
        self.inputLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputLabel.setWordWrap(True)
        self.inputLabel.setObjectName("inputLabel")

        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(450, 190, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.outputLabel.setWordWrap(True)
        self.outputLabel.setObjectName("outputLabel")

        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(320, 90, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyLabel.setFont(font)
        self.keyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.keyLabel.setObjectName("keyLabel")

        self.encryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptButton.setGeometry(QtCore.QRect(40, 720, 381, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.encryptButton.setFont(font)
        self.encryptButton.setObjectName("encryptButton")

        self.decryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.decryptButton.setGeometry(QtCore.QRect(450, 720, 381, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.decryptButton.setFont(font)
        self.decryptButton.setObjectName("decryptButton")

        self.programName = QtWidgets.QLabel(self.centralwidget)
        self.programName.setGeometry(QtCore.QRect(500, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programName.setFont(font)
        self.programName.setObjectName("programName")

        self.keyBox = QtWidgets.QLineEdit(self.centralwidget)
        self.keyBox.setGeometry(QtCore.QRect(320, 120, 921, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.keyBox.setFont(font)
        self.keyBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.keyBox.setObjectName("keyBox")

        self.keyBox.setMaxLength(2147483647)
        reg_ex = QtCore.QRegExp("[a-z, A-Z]*")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.keyBox)
        self.keyBox.setValidator(input_validator)

        self.langLabel = QtWidgets.QLabel(self.centralwidget)
        self.langLabel.setGeometry(QtCore.QRect(40, 90, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.langLabel.setFont(font)
        self.langLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.langLabel.setObjectName("langLabel")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 120, 251, 41))
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
        self.outputForm.setGeometry(QtCore.QRect(860, 240, 381, 451))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputForm.setFont(font)
        self.outputForm.setObjectName("outputForm")

        self.inputForm2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputForm2.setGeometry(QtCore.QRect(450, 240, 381, 461))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.inputForm2.setFont(font)
        self.inputForm2.setPlaceholderText("")
        self.inputForm2.setObjectName("inputForm2")

        self.outputLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel2.setGeometry(QtCore.QRect(860, 190, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.outputLabel2.setFont(font)
        self.outputLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.outputLabel2.setWordWrap(True)
        self.outputLabel2.setObjectName("outputLabel2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._mutex = QMutex()
        self.addFunctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифровние Виженера"))
        self.inputForm.setPlaceholderText(_translate("MainWindow", "Введите текст..."))
        self.inputLabel.setText(_translate("MainWindow", "Исходный текст:"))
        self.outputLabel.setText(_translate("MainWindow", "Результат шифрования:"))
        self.keyLabel.setText(_translate("MainWindow", "Ключ:"))
        self.encryptButton.setText(_translate("MainWindow", "Зашифровать"))
        self.decryptButton.setText(_translate("MainWindow", "Расшифровать"))
        self.programName.setText(_translate("MainWindow", "Шифрование Виженера"))
        self.keyBox.setPlaceholderText(_translate("MainWindow", "Введите ключ..."))
        self.langLabel.setText(_translate("MainWindow", "Язык:"))
        self.eng.setText(_translate("MainWindow", "Английский"))
        self.rus.setText(_translate("MainWindow", "Русский"))
        self.outputLabel2.setText(_translate("MainWindow", "Расшифровка:"))

    def addFunctions(self):
        self._mutex.lock()
        self.keyBox.textEdited.connect(self.keyBoxValidation)
        self.eng.clicked.connect(self.setEngKey)
        self.rus.clicked.connect(self.setRusKey)
        self.encryptButton.clicked.connect(self.crypt)
        self.decryptButton.clicked.connect(self.decrypt)

    def keyBoxValidation(self):
        self.keyBox.setText(self.keyBox.text().upper())

    def setEngKey(self):
        if (len(re.search('[А-Я]*', self.keyBox.text()).group(0)) > 0):
            self.keyBox.clear()
        reg_ex = QtCore.QRegExp("[A-Z, a-z]*")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.keyBox)
        self.keyBox.setValidator(input_validator)

    def setRusKey(self):
        if (len(re.search('[A-Z]*', self.keyBox.text()).group(0)) > 0):
            self.keyBox.clear()
        reg_ex = QtCore.QRegExp("[А-Я, а-я]*")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.keyBox)
        self.keyBox.setValidator(input_validator)


    def crypt(self):
        text = self.inputForm.toPlainText()
        key = self.keyBox.text()
        if (len(key) <= 0 or len(text) <= 0):
            return
        if self.rus.isChecked():
            alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"
        else:
            alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        # дальше должен идти алгоритм шифрования
        print(text)
        self.inputForm2.clear()
        self.inputForm2.appendPlainText(text)


    def decrypt(self):
        text = self.inputForm2.toPlainText()
        key = self.keyBox.text()
        if (len(key) <= 0 or len(text) <= 0):
            return
        if self.rus.isChecked():
            alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"
        else:
            alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        #дальше должен идти алгоритм расшифрования
        print(text)
        self.outputForm.setText(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
