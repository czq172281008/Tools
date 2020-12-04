# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QStackedWidget 例子


'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import CreatWidget
from CreatWidget import Example


class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        screen = QDesktopWidget().screenGeometry()
        # 绝对布局
        self.move(0, 0)
        self.resize(screen.width(), screen.height()-70)
        #窗口名称
        self.setWindowTitle("万能工具集")

        self.leftlist = QListWidget()

        self.leftlist.insertItem(0, '单据信息')
        self.leftlist.insertItem(1, '用户信息')
        self.leftlist.insertItem(2, '流程信息')
        self.leftlist.insertItem(3, '测试窗体')

        #绝对布局
        # self.leftlist.move(55,20)
        # self.leftlist.resize(55, 20)

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()


        self.stack1UI()
        self.stack2UI()
        self.stack3UI()


        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(Example())

        hbox = QHBoxLayout(self)#水平布局
        hbox.addWidget(self.leftlist)#左侧菜单
        #控件伸缩量
        #hbox.addStretch(4)
        hbox.addWidget(self.Stack,1,Qt.AlignLeft)#右侧面板
        self.setLayout(hbox)
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
    sys.exit(app.exec_())
