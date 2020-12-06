# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DjInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1126, 856)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 351, 111))
        self.groupBox.setObjectName("groupBox")
        self.DB_ZS = QtWidgets.QRadioButton(self.groupBox)
        self.DB_ZS.setGeometry(QtCore.QRect(190, 20, 59, 16))
        self.DB_ZS.setObjectName("DB_ZS")
        self.DB_CS = QtWidgets.QRadioButton(self.groupBox)
        self.DB_CS.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.DB_CS.setChecked(True)
        self.DB_CS.setObjectName("DB_CS")
        self.DB_BX = QtWidgets.QRadioButton(self.groupBox)
        self.DB_BX.setGeometry(QtCore.QRect(100, 20, 61, 16))
        self.DB_BX.setObjectName("DB_BX")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label.setObjectName("label")
        self.F_DJBH = QtWidgets.QLineEdit(self.groupBox)
        self.F_DJBH.setGeometry(QtCore.QRect(80, 50, 171, 20))
        self.F_DJBH.setObjectName("F_DJBH")
        self.bt_Search = QtWidgets.QPushButton(self.groupBox)
        self.bt_Search.setGeometry(QtCore.QRect(260, 50, 75, 20))
        self.bt_Search.setObjectName("bt_Search")
        self.DataTable = QtWidgets.QTableView(Form)
        self.DataTable.setGeometry(QtCore.QRect(40, 150, 981, 192))
        self.DataTable.setObjectName("DataTable")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "数据库"))
        self.DB_ZS.setText(_translate("Form", "正式库"))
        self.DB_CS.setText(_translate("Form", "测试库"))
        self.DB_BX.setText(_translate("Form", "并行库"))
        self.label.setText(_translate("Form", "单据编号："))
        self.bt_Search.setText(_translate("Form", "查询"))
