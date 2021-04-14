# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WelForm(object):
    def setupUi(self, WelForm):
        WelForm.setObjectName("WelForm")
        WelForm.resize(917, 765)
        self.label = QtWidgets.QLabel(WelForm)
        self.label.setGeometry(QtCore.QRect(150, 200, 591, 131))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(WelForm)
        self.label_2.setGeometry(QtCore.QRect(360, 410, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(WelForm)
        QtCore.QMetaObject.connectSlotsByName(WelForm)

    def retranslateUi(self, WelForm):
        _translate = QtCore.QCoreApplication.translate
        WelForm.setWindowTitle(_translate("WelForm", "Form"))
        self.label.setText(_translate("WelForm", "共享服务万能工具箱"))
        self.label_2.setText(_translate("WelForm", "V.1.0"))
