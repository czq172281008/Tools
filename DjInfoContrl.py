import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QTableView

import QTableInfo
import DjInfo
import QTableInfo
#继承页面DjInfo.Ui_Form
class ControlCode(QWidget,DjInfo.Ui_Form):
    sendmsg = pyqtSignal(object)

    def __init__(self):
        QWidget.__init__(self)
        DjInfo.Ui_Form.__init__(self)
        qb=QTableInfo.BookStorageViewer()
        self.layout = QtWidgets.QGridLayout()
        self.setupUi(self)
        self.setLayout(self.layout)

        self.DataTable.setVisible(False)
        self.bt_Search.clicked.connect(lambda: self.on_save())


    def on_save(self):
        if(self.F_DJBH.text()==''):
            self.DataTable.setVisible(False)
            btncont = self.layout.count()
            widget = QtWidgets.QTableView()
            # self.widget.setGeometry(10, 10, 380, 240)
            self.layout.addWidget(widget)
            widget2 = QtWidgets.QTableView()
            self.layout.addWidget(widget2)
            # qb = QTableInfo.BookStorageViewer()
            # qb.show()
            # QMessageBox.information(self, "单据编号",
            #                     self.tr("单据编号为空"))

        else:
            self.DataTable.setVisible(True)
            QMessageBox.information(self, "单据编号",
                                    self.tr("哈哈"))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = ControlCode()
    md.show()
    sys.exit(app.exec_())
