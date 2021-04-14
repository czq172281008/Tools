# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildrenForm4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1076, 824)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(150, 80, 771, 361))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.radioButton = QtWidgets.QRadioButton(self.splitter)
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(self.splitter)
        self.checkBox.setObjectName("checkBox")
        self.toolButton = QtWidgets.QToolButton(self.splitter)
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.toolButton.setText(_translate("Form", "按钮"))
