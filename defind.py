import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt

(form_class, qtbase_class) = uic.loadUiType('widget.ui')
#调用Qtcreator生成的界面，我喜欢这么用，也可以直接将ui界面转码成.py文件调用
class Widget(form_class, qtbase_class):
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)
        self.widget2 = QtWidgets.QWidget()
        #再生成一个QWidget子窗口
        self.song = QtWidgets.QLabel('难得')
        #生成一个QLabel控件
        self.art = QtWidgets.QLabel('安来宁')
        self.download = QtWidgets.QToolButton()
        #生成一个QToolButtonStyle按钮用于存放一个自定义按钮
        self.download.setToolButtonStyle(Qt.ToolButtonIconOnly)
        #设置按钮只显示图标
        self.download.setIconSize(QSize(20,20))
        #设置按钮大小
        self.download.setIcon(QIcon('timg.jpg'))
        #设置按钮图片样式
        self.download.setStyleSheet('background-color:transparent')
        #设置按钮样式背景透明
        self.gridlayout = QtWidgets.QGridLayout()
        #生成一个QGridLayout栅栏布局
        self.gridlayout.addWidget(self.song,0,0)
        #将之前生成的控件加入到布局中
        self.gridlayout.addWidget(self.art,0,1)
        self.gridlayout.addWidget(self.download,0,2)

        self.widget2.setLayout(self.gridlayout)
        #将布局放到开始生成的子窗口中
        '''重要部分'''
        self.listwidgetitem = QtWidgets.QListWidgetItem()
        #生成一个QListWidgetItem列表控件
        self.listwidgetitem.setSizeHint(QSize(40,40))
        #设置listwidgetitem的大小，防止显示不完全
        self.listWidget.addItem(self.listwidgetitem)
        #将listWidgetitem加入到主窗口的列表中
        self.listWidget.setItemWidget(self.listwidgetitem,self.widget2)
        #将子窗口与listWidgetitem进行连接
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Widget()
    ui.show()
    sys.exit(app.exec_())