#!/usr/bin/env python

import sys

from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtWidgets import QTreeWidgetItem


class MyTreeItem(QTreeWidgetItem):

    def __init__(self, s, parent=None):

        super(MyTreeItem, self).__init__(parent, [s])


class MyTree(QTreeWidget):

    def __init__(self, parent=None):

        super(MyTree, self).__init__(parent)
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)


        # 设置表头信息：隐藏表头
        self.setHeaderHidden(1)

        # 添加2个同级Item到QTreeWidget里面
        for s in ['child1', 'child2']:
            MyTreeItem(s, self)
        # self.connect(self, pyqtSignal('itemClicked(QTreeWidgetItem*, int)'), self.onClick)

        # QTreeWidget中每个Item的信号与槽的连接
        self.itemClicked['QTreeWidgetItem*', 'int'].connect(self.onClick)

    def onClick(self, item, column):

        # 输出鼠标选中的item名字和所在列数；其中text(column)表示第 column 列的item名字
        print(item.text(column), column)


class MainWindow(QMainWindow):

    def __init__(self, parent = None):

        super(MainWindow, self).__init__(parent)
        self.tree = MyTree(self)
        self.resize(500, 500)


def main():

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()