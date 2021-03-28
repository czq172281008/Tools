
import sys
from PyQt5 import QtWidgets,QtCore

from SpliterQW import mainWindow


class mainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('套利交易监控')
        # 菜单栏
        menu_control = self.menuBar().addMenu('菜单')
        # 开始
        act_start = menu_control.addAction('开始')
        act_start.triggered.connect(self.StartRun)
        # 退出
        act_quit = menu_control.addAction('退出')
        act_quit.triggered.connect(self.close)
        # 帮助(版权关于)
        menu_help = self.menuBar().addMenu('帮助')
        act_about = menu_help.addAction('版权')
        act_about.triggered.connect(self.about)
        act_aboutqt = menu_help.addAction('关于')
        act_aboutqt.triggered.connect(self.aboutqt)
        # 状态栏
        self.statusBar().showMessage('程序已经就绪...')
        #######################  布局   #####################
        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Vertical)  # 第一列布局（AH，商品（长期），回购）
        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)  # 第二列布局（50,300,500，T-TF，玉米）
        splitter3 = QtWidgets.QSplitter(QtCore.Qt.Vertical)  # 第三列布局（可转债，期权）

        Modules1 = QtWidgets.QTableWidget(8, 9)
        Modules2= QtWidgets.QTableWidget(8, 9)
        Modules3 = QtWidgets.QTableWidget(4, 5)
        Modules4 = QtWidgets.QTableWidget(8, 9)
        Modules5 = QtWidgets.QTableWidget(4, 5)
        Modules6 = QtWidgets.QTableWidget(8, 9)
        Modules7 = QtWidgets.QTableWidget(4, 5)
        Modules8 = QtWidgets.QTableWidget(8, 9)
        Modules9 = QtWidgets.QTableWidget(8, 9)
        Modules10 = QtWidgets.QTableWidget(4, 5)

        Modules1.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)
        Modules2.setFrameStyle(QtWidgets.QFrame.Box   |QtWidgets.QFrame.Plain)
        Modules3.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)
        Modules4.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)
        Modules5.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)
        Modules6.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)
        Modules7.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)
        Modules8.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)
        Modules9.setFrameStyle(QtWidgets.QFrame.Box   |QtWidgets.QFrame.Plain)
        Modules10.setFrameStyle(QtWidgets.QFrame.Box  | QtWidgets.QFrame.Plain)

        splitter1.addWidget(Modules1)
        splitter1.addWidget(Modules2)
        splitter1.addWidget(Modules3)

        splitter2.addWidget(Modules4)
        splitter2.addWidget(Modules5)
        splitter2.addWidget(Modules6)
        splitter2.addWidget(Modules7)
        splitter2.addWidget(Modules8)

        splitter3.addWidget(Modules9)
        splitter3.addWidget(Modules10)

        vbox1 = QtWidgets.QVBoxLayout()
        vbox1.addWidget(splitter1)
        vbox2 = QtWidgets.QVBoxLayout()
        vbox2.addWidget(splitter2)
        vbox3 = QtWidgets.QVBoxLayout()
        vbox3.addWidget(splitter3)

        Hbox = QtWidgets.QHBoxLayout()
        Hbox.addLayout(vbox1, 2)
        Hbox.addLayout(vbox2, 1)
        Hbox.addLayout(vbox3, 2)
        self.setLayout(Hbox)

        ####################### 添加模块 ######################
        ## AH模块

        ## 商品（长周期套利监控）

        ## 回购模块

        ## 期货模块
        # 50

        # 300

        # 500

        # 国债期货（T-TF）

        # 玉米

        # 棉花面纱

        ## 可转债

        ## 期权




    def about(self):
        QtWidgets.QMessageBox.about(self, 'xx投资管理有限责任公司', '量化投资部')

    def aboutqt(self):
        QtWidgets.QMessageBox.aboutQt(self)
        # self.setWindowIcon(QIcon('logo.png'))  # 后续加个图标

    def closeEvent(self, event):
        # 重新定义 closeEvent
        reply = QtWidgets.QMessageBox.question(self, '信息', '确定要退出吗？', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def StartRun(self): # 开始运行整个程序
        pass


if __name__ == '__main__':
    myapp = QtWidgets.QApplication(sys.argv)
    mainwindow = mainWindow()
    mainwindow.show()
    sys.exit(myapp.exec_())









