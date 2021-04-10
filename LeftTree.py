#左侧树结构 可以继承class LTree(QMainWindow)或 class LTree(QWidget)
import sys
from PyQt5.QtWidgets import QApplication,QMessageBox,QComboBox,QHeaderView,QWidget,QVBoxLayout,QTreeWidget,QTreeWidgetItem,QAbstractItemView
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtCore import Qt

class LTree (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('demo')
        # self.setGeometry(300,300,300,200)
        layout=QVBoxLayout()
        self.setLayout(layout)

        #------QTreeWidget------
        tree=QTreeWidget()
        layout.addWidget(tree)  #将组件添加到界面
        tree.setColumnCount(2)
        tree.setHeaderLabels(['key','value'])

        #添加根目录
        root=QTreeWidgetItem(tree)
        #设置key
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('new.png'))
        #设置value
        root.setText(1,'根节点的值')
        #添加子目录的两种方式，第一种
        child1=QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setCheckState(0,Qt.Unchecked)  #设置选中状态
        child1.setBackground(0,QColor(205,201,201))
        #第二种
        child2=QTreeWidgetItem()
        child2.setText(0,'子节点2')
        root.addChild(child2)
        #添加2层子节点
        child1_1=QTreeWidgetItem(child1)
        child1_1.setText(0,'子节点1的子节点')
        child1_1.setIcon(0,QIcon('open.png'))
        #添加点击事件
        tree.clicked.connect(self.Tree_Clicked)
    def Tree_Clicked(self,currentindex):
        print(currentindex.data())   #和下面两句相等
        print(self.sender().currentItem().text(0)) #获取点击的key的值
        print(self.sender().currentItem().text(1)) #获取点击的value的值



if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = LTree()
    tree.show()
    sys.exit(app.exec_())
