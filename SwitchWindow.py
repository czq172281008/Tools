#程序窗体跳转总管
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
                             QToolBox, QPushButton, QLabel,
                             QTreeWidget, QTreeWidgetItem)
from PyQt5.QtGui import QIcon, QPixmap
from FORM.ChildrenForm2 import Ui_Form2
from FORM.ChildrenForm3_Action import ChildrenForm3_Busi
from FORM.ChildrenForm4 import Ui_Form4
from FORM.RightEntity import RightEn
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
        # 创建一个QTreeWidget部件
        self.tree = QTreeWidget()

        # 设置部件的列数为1
        self.tree.setColumnCount(1)

        # 设置头部信息，因为上面设置列数为2，所以要设置两个标识符
        # self.tree.setHeaderLabels(['节点名称'])

        # 设置表头信息：隐藏表头
        self.tree.setHeaderHidden(1)

        # 设置root和root2为self.tree的子树，所以root和root2就是跟节点
        root = QTreeWidgetItem(self.tree)
        root2 = QTreeWidgetItem(self.tree)

        # 设置root节点的打开/关闭状态下的不同的图片
        icon = QIcon()
        # 节点打开状态
        icon.addPixmap(QPixmap("./FORM/folder open.png"), QIcon.Normal, QIcon.On)
        # 节点关闭状态　　
        icon.addPixmap(QPixmap("./FORM/folder closed.png"), QIcon.Normal, QIcon.Off)
        root.setIcon(0, icon)

        # 设置根节点的名称
        root.setText(0, '共享服务平台')
        root2.setText(0, 'FMIS平台')

        # 给根节点设置备注和说明；相当于给根节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        root.setWhatsThis(0, '共享服务平台')
        root2.setWhatsThis(0, 'FMIS平台')

        # 为root节点设置子结点
        child11 = QTreeWidgetItem(root)

        # 给root节点的第一个子节点设置备注和说明；相当于给第一个节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        child11.setWhatsThis(0, '第一节点_child1')

        # 设置child1节点的图片
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./FORM/Point.png"), QIcon.Normal)
        child11.setIcon(0, icon2)

        child11.setText(0, 'child1')
        # child1.setText(1, 'name1')
        child12 = QTreeWidgetItem(root)
        # 设置child2节点的图片
        child12.setIcon(0, icon2)
        child12.setText(0, 'child2')

        # 给root节点的第二个子节点设置备注和说明；相当于给第二个节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        child12.setWhatsThis(0, '第一节点_child2')

        # child2.setText(1, 'name2')
        child13 = QTreeWidgetItem(root)

        # 设置child3节点的打开 / 关闭状态下的不同的图片
        child13.setIcon(0, icon)

        child13.setText(0, 'child3')

        # 给root节点的第三个子节点设置备注和说明；相当于给第三个节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        child13.setWhatsThis(0, '第一节点_child3')

        child134 = QTreeWidgetItem(child13)
        # 设置child4节点的图片
        child134.setIcon(0, icon2)
        child134.setText(0, 'child4')

        # 给root节点的第三个子节点的第一个子节点设置备注和说明；相当于给该节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        child134.setWhatsThis(0, '第一节点_child3_child4')

        # child4.setText(1, 'name4')

        # 为root2节点设置子结点
        child21 = QTreeWidgetItem(root2)
        child21.setText(0, 'child1')
        child21.setWhatsThis(0, '第二节点_child1')
        # child1.setText(1, 'name1')
        child22 = QTreeWidgetItem(root2)
        child22.setText(0, 'child2')
        child22.setWhatsThis(0, '第二节点_child2')
        # child2.setText(1, 'name2')
        child23 = QTreeWidgetItem(root2)
        child23.setText(0, 'child3')
        child23.setWhatsThis(0, '第二节点_child3')
        child234 = QTreeWidgetItem(child23)
        child234.setText(0, 'child4')
        child234.setWhatsThis(0, '第二节点_child3_child4')

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

        # QTreeWidget中每个Item的信号与槽的连接
        self.tree.itemClicked['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 点击（包括选中，也包括checkbox选择）
        # self.tree.itemPressed['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 点击选中（不包括checkbox选择）
        # self.tree.itemChanged['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 状态变更就会响应，也包括程序置的状态，使用时需要注意


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