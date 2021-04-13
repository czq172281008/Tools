#程序窗体跳转总管
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
                             QToolBox, QPushButton, QLabel,
                             QTreeWidget, QTreeWidgetItem)
from PyQt5.QtGui import QIcon, QPixmap
from FORM.ChildrenForm2 import Ui_Form2
from FORM.ChildrenForm3_Action import ChildrenForm3_Busi
from FORM.ChildrenForm4 import Ui_Form4
from FORM.RightEntity import RightEn
from LeftTree import LTree
import sys

from treetable import *#窗体和逻辑分离

class SwitchMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(SwitchMainForm, self).__init__(parent)

        # 主窗口初始化时实现主窗口布局
        self.setupUi(self)

        # 调用该类自己设定的初始化方法
        self.iniUI()

    # 设定该类自己的初始化方法
    def iniUI(self):

        # self.splitter.setGeometry(QtCore.QRect(10, 10, 700, 871))

        self.tree=LTree()
        self.tree.sendmsg.connect(self.onClick)#接收信号绑定本对象中槽函数

        # 给QSsplitter添加第一个窗体（QTreeWidget）
        self.splitter.addWidget(self.tree)

        # 主窗口初始化时实例化子窗口1和子窗口2
        self.RE = RightEn()
        self.child2 = ChildrenForm2()
        self.child3 = ChildrenForm3()
        self.child4 = ChildrenForm4()

        # 在主窗口的QSplitter里添加子窗口
        self.splitter.addWidget(self.RE)

        # 设置分割器QSplitter初始化时各个子窗体的大小；下面是两个子窗体。
        self.splitter.setSizes([180, 700])

        #  下面一行为设置 QSplitter 分割器伸缩大小因子，但是这样设置全屏后导航栏放大了比较好看；不清楚原因。
        self.splitter.setStretchFactor(0, 0)  # 此函数用于设定：控件是否可伸缩。第一个参数用于指定控件的序号。第二个函数大于0时，表示控件可伸缩，小于0时，表示控件不可伸缩。
        self.splitter.setStretchFactor(1, 1)  # 此函数用于设定：控件是否可伸缩。第一个参数用于指定控件的序号。第二个函数大于0时，表示控件可伸缩，小于0时，表示控件不可伸缩。

        #  设置 QSplitter 分割器各部分最小化时的情况，设置为“False”意味着左右拉动分隔栏时各部分不会消失；此设置也可以在界面设计时在 QtDesigner 里设置。
        self.splitter.setChildrenCollapsible(False)

        #  设置 QSplitter 分割器随主窗口自适应大小变化。此设置也可以在界面设计时在 QtDesigner 里设置。
        self.splitter.setAutoFillBackground(True)



    # QTreeWidget中每个Item的信号与槽的连接；对应的槽函数；输出鼠标选中的item名字和所在列数；其中text(column)表示第 column 列的item名字
    def onClick(self, item, column):

        # 控制台输出鼠标选中的item名字和所在列数；其中text(column)表示第 column 列的item名字
        print(item.text(column), column)
        print(item.whatsThis(column))

        if item.whatsThis(column) == '共享服务':
            # 把QSplitter的指定位置的窗体从QSplitter中剥离
            self.splitter.widget(1).setParent(None)
            # 在QSplitter的指定位置载入新窗体，但要先用上面的“self.splitter.widget(1).setParent(None)”命令。
            self.splitter.insertWidget(1, self.RE)
            self.splitter.setStretchFactor(0, 0)  # 此函数用于设定：控件是否可伸缩。第一个参数用于指定控件的序号。第二个函数大于0时，表示控件可伸缩，小于0时，表示控件不可伸缩。
            self.splitter.setStretchFactor(1, 1)  # 此函数用于设定：控件是否可伸缩。第一个参数用于指定控件的序号。第二个函数大于0时，表示控件可伸缩，小于0时，表示控件不可伸缩。
            #  设置 QSplitter 分割器各部分最小化时的情况，设置为“False”意味着左右拉动分隔栏时各部分不会消失；此设置也可以在界面设计时在 QtDesigner 里设置。
            self.splitter.setChildrenCollapsible(False)
            #  设置 QSplitter 分割器随主窗口自适应大小变化。此设置也可以在界面设计时在 QtDesigner 里设置。
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第一节点_child1':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.child2)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第一节点_child2':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.child3)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第一节点_child3':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.RE)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第一节点_child3_child4':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.child2)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == 'FMIS平台':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.child3)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第二节点_child1':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.RE)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第二节点_child2':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.child2)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第二节点_child3':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.child3)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)
        elif item.whatsThis(column) == '第二节点_child3_child4':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.child4)
            self.splitter.setStretchFactor(0, 0)
            self.splitter.setStretchFactor(1, 1)
            self.splitter.setChildrenCollapsible(False)
            self.splitter.setAutoFillBackground(True)


# class ChildrenForm(QWidget, Ui_Form):
#     def __init__(self):
#         super(ChildrenForm, self).__init__()
#
#         # 子窗口初始化时实现子窗口布局
#         self.setupUi(self)
#
#         # 设置子窗体最小尺寸
#         self.setMinimumWidth(30)
#         self.setMinimumHeight(30)


class ChildrenForm2(QWidget, Ui_Form2):
    def __init__(self):
        super(ChildrenForm2, self).__init__()

        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)


class ChildrenForm3(QWidget, ChildrenForm3_Busi):
    def __init__(self):
        super(ChildrenForm3, self).__init__()

        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)
        self.setupBusi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)

class ChildrenForm4(QWidget, Ui_Form4):
    def __init__(self):
        super(ChildrenForm4, self).__init__()

        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    myshow = SwitchMainForm()
    myshow.show()
    sys.exit(app.exec_())