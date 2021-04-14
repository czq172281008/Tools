import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QFrame, QSplitter, \
    QTextEdit

from UI.MainForm import Ui_MainWindow

class Test1(QWidget,Ui_MainWindow):#继承QTDesigner绘制窗体文件单独页面DjInfo.Ui_Form实现界面和逻辑分离
    sendmsg = pyqtSignal(object)

    def __init__(self, parent=None):
        super(Test1, self).__init__(parent)#可替换成# super().__init__() # QWidget.__init__(self)
        # QWidget.__init__(self)
        # QWidget.__init__(self)
        # qb=QTableInfo.BookStorageViewer()
        self.setupUi(self)#初始化DjInfo.Ui_Form

        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)


    def on_save(self):
        if(self.F_DJBH.text()==''):
            self.DataTable.setVisible(False)
            btncont = self.layout.count()
            widget = QtWidgets.QTableView()
            # self.widget.setGeometry(10, 10, 380, 240)
            self.layout.addWidget(widget)
            widget2 = QtWidgets.QTableView()
            self.layout.addWidget(widget2)

            topleft = QFrame()
            topleft.setFrameShape(QFrame.StyledPanel)

            bottom = QFrame()
            bottom.setFrameShape(QFrame.StyledPanel)

            splitter1 = QSplitter()
            textedit = QTextEdit()
            splitter1.addWidget(topleft)
            splitter1.addWidget(textedit)
            splitter1.setSizes([200, 100])

            splitter2 = QSplitter()
            splitter2.addWidget(splitter1)
            splitter2.addWidget(bottom)

            widget2 = QWidget()
            song = QtWidgets.QLabel('难得')
            gridlayout = QtWidgets.QGridLayout()
            gridlayout.addWidget(song, 0, 0)
            widget2.setLayout(gridlayout)

            self.layout.addWidget(splitter2)
            self.layout.addWidget(splitter2)
            self.layout.addWidget(splitter2)
            self.layout.addWidget(widget2)

            # QW1 = QWidget()
            # DjinfoW1 = ttt.Czq()
            #
            # DjinfoW1.setupUi(QW1)  # 将子页面添加到对应控件QW变量
            # gridlayout1 = QtWidgets.QGridLayout()
            # QW1.setLayout(gridlayout1)
            # self.layout.addWidget(QW1)

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
    md = Test1()
    md.show()
    sys.exit(app.exec_())
