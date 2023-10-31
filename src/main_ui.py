from PyQt6 import QtCore, QtWidgets, QtGui
import os
from knn import KNN

import pandas as pd


class Ui_Dialog(QtWidgets.QDialog):
    data: pd.DataFrame = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 276)
        self.param1 = QtWidgets.QLineEdit(parent=Dialog)
        self.param1.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.param1.setObjectName("param1")
        self.param1.setValidator(QtGui.QDoubleValidator())

        self.param2 = QtWidgets.QLineEdit(parent=Dialog)
        self.param2.setGeometry(QtCore.QRect(10, 60, 191, 31))
        self.param2.setObjectName("param2")
        self.param2.setValidator(QtGui.QDoubleValidator())

        self.param3 = QtWidgets.QLineEdit(parent=Dialog)
        self.param3.setGeometry(QtCore.QRect(10, 100, 191, 31))
        self.param3.setObjectName("param3")
        self.param3.setValidator(QtGui.QDoubleValidator())

        self.param4 = QtWidgets.QLineEdit(parent=Dialog)
        self.param4.setGeometry(QtCore.QRect(10, 140, 191, 31))
        self.param4.setObjectName("param4")
        self.param4.setValidator(QtGui.QDoubleValidator())

        self.weightForParam1 = QtWidgets.QLineEdit(parent=Dialog)
        self.weightForParam1.setGeometry(QtCore.QRect(210, 20, 51, 31))
        self.weightForParam1.setObjectName("weightForParam1")
        self.weightForParam1.setValidator(QtGui.QIntValidator())
        self.weightForParam1.setText("1")

        self.weightForParam2 = QtWidgets.QLineEdit(parent=Dialog)
        self.weightForParam2.setGeometry(QtCore.QRect(210, 60, 51, 31))
        self.weightForParam2.setObjectName("weightForParam2")
        self.weightForParam2.setValidator(QtGui.QIntValidator())
        self.weightForParam2.setText("1")

        self.weightForParam3 = QtWidgets.QLineEdit(parent=Dialog)
        self.weightForParam3.setGeometry(QtCore.QRect(210, 100, 51, 31))
        self.weightForParam3.setObjectName("weightForParam3")
        self.weightForParam3.setValidator(QtGui.QIntValidator())
        self.weightForParam3.setText("1")

        self.weightForParam4 = QtWidgets.QLineEdit(parent=Dialog)
        self.weightForParam4.setGeometry(QtCore.QRect(210, 140, 51, 31))
        self.weightForParam4.setObjectName("weightForParam4")
        self.weightForParam4.setValidator(QtGui.QIntValidator())
        self.weightForParam4.setText("1")

        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 51, 20))
        self.label_2.setObjectName("label_2")
        self.normalizationGroupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.normalizationGroupBox.setGeometry(QtCore.QRect(270, 70, 161, 71))
        self.normalizationGroupBox.setObjectName("normalizationGroupBox")
        self.normalizeYesRadioButton = QtWidgets.QRadioButton(parent=self.normalizationGroupBox)
        self.normalizeYesRadioButton.setGeometry(QtCore.QRect(10, 20, 89, 20))
        self.normalizeYesRadioButton.setObjectName("normalizeYesRadioButton")
        self.normalizeNoRadioButton = QtWidgets.QRadioButton(parent=self.normalizationGroupBox)
        self.normalizeNoRadioButton.setGeometry(QtCore.QRect(10, 40, 89, 20))
        self.normalizeNoRadioButton.setObjectName("normalizeNoRadioButton")
        self.normalizeNoRadioButton.setChecked(True)
        self.weightedVotingGroupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.weightedVotingGroupBox.setGeometry(QtCore.QRect(270, 150, 161, 71))
        self.weightedVotingGroupBox.setObjectName("weightedVotingGroupBox")
        self.weightedVotingYesRadioButton = QtWidgets.QRadioButton(parent=self.weightedVotingGroupBox)
        self.weightedVotingYesRadioButton.setGeometry(QtCore.QRect(10, 20, 89, 20))
        self.weightedVotingYesRadioButton.setObjectName("weightedVotingYesRadioButton")
        self.weightedVotingNoRadioButton = QtWidgets.QRadioButton(parent=self.weightedVotingGroupBox)
        self.weightedVotingNoRadioButton.setGeometry(QtCore.QRect(10, 40, 89, 20))
        self.weightedVotingNoRadioButton.setObjectName("weightedVotingNoRadioButton")
        self.weightedVotingNoRadioButton.setChecked(True)

        self.kValueGroupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.kValueGroupBox.setGeometry(QtCore.QRect(270, 220, 161, 51))
        self.kValueGroupBox.setObjectName("kValueGroupBox")

        self.kValueTextEdit = QtWidgets.QLineEdit(parent=self.kValueGroupBox)
        self.kValueTextEdit.setGeometry(QtCore.QRect(0, 20, 161, 31))
        self.kValueTextEdit.setObjectName("kValueTextEdit")
        self.kValueTextEdit.setValidator(QtGui.QIntValidator())
        self.kValueTextEdit.setText("5")

        self.calculateButton = QtWidgets.QPushButton(parent=Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(10, 180, 251, 41))
        self.calculateButton.setObjectName("calculateButton")

        self.answerGroupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.answerGroupBox.setGeometry(QtCore.QRect(10, 220, 251, 51))
        self.answerGroupBox.setObjectName("answerGroupBox")

        self.answerTextEdit = QtWidgets.QTextEdit(parent=self.answerGroupBox)
        self.answerTextEdit.setGeometry(QtCore.QRect(0, 20, 421, 31))
        self.answerTextEdit.setReadOnly(True)
        self.answerTextEdit.setObjectName("answerTextEdit")

        self.loadDataButton = QtWidgets.QPushButton(parent=Dialog)
        self.loadDataButton.setGeometry(QtCore.QRect(270, 20, 161, 41))
        self.loadDataButton.setObjectName("loadDataButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Knn"))
        self.label.setText(_translate("Dialog", "Параметры"))
        self.label_2.setText(_translate("Dialog", "Веса"))
        self.normalizationGroupBox.setTitle(_translate("Dialog", "Нормализовать?"))
        self.normalizeYesRadioButton.setText(_translate("Dialog", "Да"))
        self.normalizeNoRadioButton.setText(_translate("Dialog", "Нет"))
        self.weightedVotingGroupBox.setTitle(_translate("Dialog", "Взвешенное голосование"))
        self.weightedVotingYesRadioButton.setText(_translate("Dialog", "Да"))
        self.weightedVotingNoRadioButton.setText(_translate("Dialog", "Нет"))
        self.kValueGroupBox.setTitle(_translate("Dialog", "Количество - K"))
        self.calculateButton.setText(_translate("Dialog", "Получить ответ"))
        self.calculateButton.clicked.connect(self.calculate_answer)

        self.answerGroupBox.setTitle(_translate("Dialog", "Ответ"))

        self.loadDataButton.setText(_translate("Dialog", "Загрузить данные"))
        self.loadDataButton.clicked.connect(self.load_data)

    def load_data(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open File",
            os.getcwd(),
            "CSV Files (*.csv);; All Files (*)"
        )[0]
        if fname:
            self.data = pd.read_csv(fname)
            print("Data loaded successfully!")

    def calculate_answer(self):
        try:
            if self.data is None:
                raise Exception("Данные не загружены")

            if not (self.param1.text() and self.param2.text() and
                    self.param3.text() and self.param4.text() and
                    self.weightForParam1.text() and self.weightForParam2.text() and
                    self.weightForParam3.text() and self.weightForParam4.text()):
                raise Exception("All input fields must be filled.")

            param1_value = float(self.param1.text())
            param2_value = float(self.param2.text())
            param3_value = float(self.param3.text())
            param4_value = float(self.param4.text())

            weight1 = int(self.weightForParam1.text())
            weight2 = int(self.weightForParam2.text())
            weight3 = int(self.weightForParam3.text())
            weight4 = int(self.weightForParam4.text())

            knn = KNN(self.data)

            result = knn.predict([param1_value, param2_value, param3_value, param4_value],
                                 weight=[weight1, weight2, weight3, weight4],
                                 k=int(self.kValueTextEdit.text()),
                                 stand=self.normalizeYesRadioButton.isChecked(),
                                 poll=self.weightedVotingYesRadioButton.isChecked())

            self.answerTextEdit.setPlainText(result)
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", str(ex))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
