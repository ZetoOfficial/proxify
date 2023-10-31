# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainjIYEge.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QGroupBox, QLabel,
                               QPushButton, QRadioButton, QTextEdit)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(436, 276)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 20, 191, 31))
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 60, 191, 31))
        self.textEdit_3 = QTextEdit(Dialog)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 100, 191, 31))
        self.textEdit_4 = QTextEdit(Dialog)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 140, 191, 31))
        self.textEdit_5 = QTextEdit(Dialog)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(210, 20, 51, 31))
        self.textEdit_6 = QTextEdit(Dialog)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(210, 60, 51, 31))
        self.textEdit_7 = QTextEdit(Dialog)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(210, 100, 51, 31))
        self.textEdit_8 = QTextEdit(Dialog)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(210, 140, 51, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 191, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 0, 51, 20))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(270, 70, 161, 71))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 20, 89, 20))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 40, 89, 20))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(270, 150, 161, 71))
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(10, 20, 89, 20))
        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(10, 40, 89, 20))
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(270, 220, 161, 51))
        self.textEdit_9 = QTextEdit(self.groupBox_3)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(0, 20, 161, 31))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 180, 251, 41))
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 220, 251, 51))
        self.textEdit_10 = QTextEdit(self.groupBox_4)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(0, 20, 421, 31))
        self.textEdit_10.setReadOnly(True)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 20, 161, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(
            QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0441\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog",
                                                          u"\u041d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u0442\u044c?",
                                                          None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog",
                                                            u"\u0412\u0437\u0432\u0435\u0448\u0435\u043d\u043d\u043e\u0435 \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435",
                                                            None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
        self.groupBox_3.setTitle(
            QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e - K",
                                       None))
        self.pushButton.setText(QCoreApplication.translate("Dialog",
                                                           u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442",
                                                           None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog",
                                                             u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c  \u0434\u0430\u043d\u043d\u044b\u0435",
                                                             None))
    # retranslateUi
