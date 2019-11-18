# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_encrypt(object):
    def setupUi(self, Dialog_encrypt):
        Dialog_encrypt.setObjectName("Dialog_encrypt")
        Dialog_encrypt.resize(800, 566)
        Dialog_encrypt.setStyleSheet("background-image: url(:/newPrefix/new.jpg);background-repeat:no-repeat")
        self.label_encrypt = QtWidgets.QLabel(Dialog_encrypt)
        self.label_encrypt.setGeometry(QtCore.QRect(120, 40, 731, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_encrypt.setFont(font)
        self.label_encrypt.setStyleSheet("background-image: url(:/newPrefix/blk.png);\n"
"color: rgb(255, 255, 255);")
        self.label_encrypt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_encrypt.setObjectName("label_encrypt")

        self.pushButton_upimg = QtWidgets.QPushButton(Dialog_encrypt)
        self.pushButton_upimg.setGeometry(QtCore.QRect(100, 120, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_upimg.setFont(font)
        self.pushButton_upimg.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_upimg.setObjectName("pushButton_upimg")

        self.pushButton_encrypt = QtWidgets.QPushButton(Dialog_encrypt)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(400, 280, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_encrypt.setFont(font)
        self.pushButton_encrypt.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")

        self.label_email = QtWidgets.QLabel(Dialog_encrypt)
        self.label_email.setGeometry(QtCore.QRect(180, 200, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_email.setFont(font)
        self.label_email.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_email.setObjectName("label_email")

        self.lineEdit_email = QtWidgets.QLineEdit(Dialog_encrypt)
        self.lineEdit_email.setGeometry(QtCore.QRect(330, 200, 351, 41))
        self.lineEdit_email.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.retranslateUi(Dialog_encrypt)
        QtCore.QMetaObject.connectSlotsByName(Dialog_encrypt)

    def retranslateUi(self, Dialog_encrypt):
        _translate = QtCore.QCoreApplication.translate
        Dialog_encrypt.setWindowTitle(_translate("Dialog_encrypt", "IMAGE ENCRYPTION"))
        self.label_encrypt.setText(_translate("Dialog_encrypt", "IMAGE ENCRYPTION"))
        self.pushButton_upimg.setText(_translate("Dialog_encrypt", "UPLOAD IMAGE"))
        self.pushButton_encrypt.setText(_translate("Dialog_encrypt", "ENCRYPT"))
        self.label_email.setText(_translate("Dialog_encrypt", "EMAIL ID"))
        self.lineEdit_email.setPlaceholderText(_translate("Dialog_encrypt", "Enter Email id of receiver"))
import Document
