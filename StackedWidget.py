# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DjInfoContrl import ControlCode
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'#处理结果集乱码


class StackedExample(QWidget):

    def __init__(self):
        super(StackedExample, self).__init__()
        self.DrawMainUI()#初始化主窗体


    def DrawMainUI(self):
        screen = QDesktopWidget().screenGeometry()
        # 绝对布局
        self.move(0, 0)
        self.resize(screen.width(), screen.height() - 70)
        # 窗口名称




        self.setWindowTitle("共享运维工具集V1.0")
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '单据信息')

        # self.leftlist.insertItem(1, '用户信息')
        # self.leftlist.insertItem(2, '流程信息')
        # self.leftlist.insertItem(1, 'QT窗体')
        # self.leftlist.insertItem(2, '手敲窗体')

        self.leftlist.setSpacing(2)  # 设置内边距---控件之间的距离

        # self.leftlist.setContentsMargins(200, 40, 40, 50)  # 设置外边距--控件到窗口边框的距离
        # 这是QLayout的指令
        # 参数1 左边距离
        # 参数2 上边距离
        # 参数3 右边距离
        # 参数4 下边距离

        # 绝对布局
        # self.leftlist.move(55,20)
        # self.leftlist.resize(55, 20)

        self.stack1 = ControlCode()
        # self.stack2 = QWidget()
        # self.stack3 = QWidget()

        # 引用单独QTDesigner绘制窗体文件
        # QW = QWidget()
        # DjinfoW = ControlCode()
        # DjinfoW.setupUi(QW)  # 将子页面添加到对应控件QW变量

        # 自定义手敲窗体
        # Ex = Example()

        # self.stack1UI()
        # self.stack2UI()
        # self.stack3UI()

        mainSplitter = QSplitter(Qt.Horizontal)
        self.Stack = QStackedWidget(mainSplitter)
        self.Stack.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        # self.Stack.addWidget(self.stack2)
        # self.Stack.addWidget(self.stack3)
        # self.Stack.addWidget(Ex)
        # self.Stack.addWidget(QW)  # 加入QTDesigner绘制窗体



        mainLayout = QHBoxLayout(self)
        # mainLayout.setMargins(5)  #对话框边距设为5 Margin 边距  5px
        # mainLayout.setSpacing(5)  #内部控件间距为5 Spacing间距  5px

        # addWidget参数2 伸缩因子：就是占用的份数(倍数)；总的分成6份，label1占1份，label2占2份，label3占3份
        # 0  不伸缩
        mainLayout.addWidget(self.leftlist, 1, Qt.AlignLeft)
        mainLayout.addWidget(self.Stack, 0)
        # #layout.addStretch(2)  #添加空白伸缩因子
        # #注意：这个空白伸缩可以压缩成0；只有足够大时才有效
        mainLayout.setStretchFactor(self.leftlist, 1)
        mainLayout.setStretchFactor(self.Stack, 10)  # 设定了leftlist与Stack比例为1:10。

        # hbox = QHBoxLayout(self)#水平布局
        # hbox.addWidget(self.leftlist)#左侧菜单
        # #控件伸缩量
        # #hbox.addStretch(4)
        # #hbox.addWidget(self.Stack,1,Qt.AlignLeft)#右侧面板
        # hbox.addWidget(self.Stack)  # 右侧面板
        # self.setLayout(hbox)

        self.leftlist.currentRowChanged.connect(self.display)

    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.stack3.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    app.exec_()
    sys.exit()
