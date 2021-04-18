'''
左侧树结构 可以继承class LTree(QMainWindow)或 class LTree(QWidget)
利用自定义信号实现左侧树与右侧显示界面分离
灵感来自于pyqt5高级编程CustomSignal.py
pyqtSignal()

'''

import sys
from PyQt5.QtWidgets import QApplication,QMessageBox,QComboBox,QHeaderView,QWidget,QVBoxLayout,QTreeWidget,QTreeWidgetItem,QAbstractItemView
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal


class LTree (QWidget):

    sendmsg = pyqtSignal(QTreeWidgetItem,int)#定义信号准备发出

    def __init__(self):
        super().__init__()#可替换成super(LTree, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('左侧树形菜单')
        # self.setGeometry(300,400,300,200)
        layout=QVBoxLayout() #不加样式布局无法显示出来树
        self.setLayout(layout)

        # 创建一个QTreeWidget部件
        self.tree = QTreeWidget()

        # 设置部件的列数为1
        self.tree.setColumnCount(1)

        # 设置头部信息，因为上面设置列数为2，所以要设置两个标识符
        # self.tree.setHeaderLabels(['节点名称'])

        # 设置表头信息：隐藏表头
        self.tree.setHeaderHidden(1)

        layout.addWidget(self.tree)  #将组件添加到界面

        # 设置root和root2为self.tree的子树，所以root和root2就是跟节点
        root = QTreeWidgetItem(self.tree)
        root2 = QTreeWidgetItem(self.tree)

        # 设置root节点的打开/关闭状态下的不同的图片
        icon = QIcon()
        # 节点打开状态
        icon.addPixmap(QPixmap("UI/folder open.png"), QIcon.Normal, QIcon.On)
        # 节点关闭状态　　
        icon.addPixmap(QPixmap("UI/folder closed.png"), QIcon.Normal, QIcon.Off)
        root.setIcon(0, icon)

        # 设置根节点的名称
        root.setText(0, '共享服务')
        root2.setText(0, 'FMIS平台')

        # 给根节点设置备注和说明；相当于给根节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        root.setWhatsThis(0, '共享服务')
        root2.setWhatsThis(0, 'FMIS平台')

        # 为root节点设置子结点
        child11 = QTreeWidgetItem(root)

        # 给root节点的第一个子节点设置备注和说明；相当于给第一个节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        child11.setWhatsThis(0, '第一节点_child1')

        # 设置child1节点的图片
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("UI/Point.png"), QIcon.Normal)
        child11.setIcon(0, icon2)

        child11.setText(0, '单据信息')
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

        # #QTreeWidget中每个Item的信号与槽的连接
        self.tree.itemClicked['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 点击（包括选中，也包括checkbox选择）
        self.tree.itemPressed['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 点击选中（不包括checkbox选择）
        self.tree.itemChanged['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 状态变更就会响应，也包括程序置的状态，使用时需要注意


    def onClick(self, item, column):#发送信号给外部实体调用槽函数
        self.sendmsg.emit(item,column)
        # print(item.text(column), column)
        # print(item.whatsThis(column))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = LTree()
    tree.show()
    sys.exit(app.exec_())
