# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decrypt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Decrypt(object):
    def setupUi(self, Decrypt):
        Decrypt.setObjectName("Decrypt")
        Decrypt.resize(800, 566)
        Decrypt.setStyleSheet("background-image: url(:/newPrefix/new.jpg);background-repeat:no-repeat")
        self.label_decrypt = QtWidgets.QLabel(Decrypt)
        self.label_decrypt.setGeometry(QtCore.QRect(120, 40, 731, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_decrypt.setFont(font)
        self.label_decrypt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-image: url(:/newPrefix/blk.png);")
        self.label_decrypt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_decrypt.setObjectName("label_decrypt")

        self.pushButton_upimg = QtWidgets.QPushButton(Decrypt)
        self.pushButton_upimg.setGeometry(QtCore.QRect(60, 150, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_upimg.setFont(font)
        self.pushButton_upimg.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_upimg.setObjectName("pushButton_upimg")

        self.pushButton_decrypt = QtWidgets.QPushButton(Decrypt)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(420, 250, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")

        self.retranslateUi(Decrypt)
        QtCore.QMetaObject.connectSlotsByName(Decrypt)

    def retranslateUi(self, Decrypt):
        _translate = QtCore.QCoreApplication.translate
        Decrypt.setWindowTitle(_translate("Decrypt", "IMAGE DECRYPTION"))
        self.label_decrypt.setText(_translate("Decrypt", "IMAGE DECRYPTION"))
        self.pushButton_upimg.setText(_translate("Decrypt", "UPLOAD IMAGE"))
        self.pushButton_decrypt.setText(_translate("Decrypt", "DECRYPT"))
import Document
