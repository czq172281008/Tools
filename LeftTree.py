#左侧树结构 可以继承class LTree(QMainWindow)或 class LTree(QWidget)
import sys
from PyQt5.QtWidgets import QApplication,QMessageBox,QComboBox,QHeaderView,QWidget,QVBoxLayout,QTreeWidget,QTreeWidgetItem,QAbstractItemView
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import Qt

class LTree (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('demo')
        # self.setGeometry(300,300,300,200)
        layout=QVBoxLayout()#不加样式控件无法显示出来
        self.setLayout(layout)

        # #------QTreeWidget------
        # tree=QTreeWidget()
        # layout.addWidget(tree)  #将组件添加到界面
        # tree.setColumnCount(2)
        # tree.setHeaderLabels(['key','value'])
        #
        # #添加根目录
        # root=QTreeWidgetItem(tree)
        # #设置key
        # root.setText(0,'根节点')
        # root.setIcon(0,QIcon('new.png'))
        # #设置value
        # root.setText(1,'根节点的值')
        # #添加子目录的两种方式，第一种
        # child1=QTreeWidgetItem(root)
        # child1.setText(0,'子节点1')
        # child1.setCheckState(0,Qt.Unchecked)  #设置选中状态
        # child1.setBackground(0,QColor(205,201,201))
        # #第二种
        # child2=QTreeWidgetItem()
        # child2.setText(0,'子节点2')
        # root.addChild(child2)
        # #添加2层子节点
        # child1_1=QTreeWidgetItem(child1)
        # child1_1.setText(0,'子节点1的子节点')
        # child1_1.setIcon(0,QIcon('open.png'))
        # #添加点击事件
        # tree.clicked.connect(self.Tree_Clicked)


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
        icon.addPixmap(QPixmap("./FORM/folder open.png"), QIcon.Normal, QIcon.On)
        # 节点关闭状态　　
        icon.addPixmap(QPixmap("./FORM/folder closed.png"), QIcon.Normal, QIcon.Off)
        root.setIcon(0, icon)

        # 设置根节点的名称
        root.setText(0, '第一节点')
        root2.setText(0, '第二节点')

        # 给根节点设置备注和说明；相当于给根节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        root.setWhatsThis(0, '第一节点')
        root2.setWhatsThis(0, '第二节点')

        # 为root节点设置子结点
        child11 = QTreeWidgetItem(root)

        # 给root节点的第一个子节点设置备注和说明；相当于给第一个节点设置了一个新名字！后面信号与槽函数连接时可以通过这个“新名字”与槽函数连接。
        child11.setWhatsThis(0, '第一节点_child1')

        # 设置child1节点的图片
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./Original Point.png"), QIcon.Normal)
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

        # #QTreeWidget中每个Item的信号与槽的连接
        # self.tree.itemClicked['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 点击（包括选中，也包括checkbox选择）
        # self.tree.itemPressed['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 点击选中（不包括checkbox选择）
        # self.tree.itemChanged['QTreeWidgetItem*', 'int'].connect(self.onClick)  # 状态变更就会响应，也包括程序置的状态，使用时需要注意

    def onClick(self, item, column):
        print(item.text(column), column)

    def Tree_Clicked(self,currentindex):
        print(currentindex.data())   #和下面两句相等
        print(self.sender().currentItem().text(0)) #获取点击的key的值
        print(self.sender().currentItem().text(1)) #获取点击的value的值



if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = LTree()
    tree.show()
    sys.exit(app.exec_())
