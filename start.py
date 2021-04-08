import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QIcon, QKeySequence
from SwitchWindow import SwitchMainForm

# class ChildrenForm2(QWidget, MainForm1):
#     def __init__(self):
#         super(ChildrenForm2, self).__init__()
#
#         # 子窗口初始化时实现子窗口布局
#         self.setupUi(self)
#
#         # 设置子窗体最小尺寸
#         self.setMinimumWidth(30)
#         self.setMinimumHeight(30)

class MdiSubWindow(QMdiSubWindow):
    def __init__(self):
        super(MdiSubWindow, self).__init__()

    def closeEvent(self, event):
        self.deleteLater()  # 关闭后删除


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.iniUI()

    def iniUI(self):
        self.mdi = QMdiArea()  # 实例化Qmidarea区域
        self.setCentralWidget(self.mdi)  # 设置为中央窗口部件
        self.createFileActions()

        menuBar = self.menuBar()  # 实例化菜单栏
        file = menuBar.addMenu('文件')  # 添加文件菜单
        # 添加子菜单
        file.addAction(self.fileNewAction)
        file.addAction(self.separator)
        file.addAction(self.exitAction)
        self.windowMenu = menuBar.addMenu("&窗口")  # 添加窗口菜单
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)  # 用于动态更新菜
        # 设置主窗口的标题
        screen = QDesktopWidget().screenGeometry()
        # 绝对布局
        self.move(0, 0)
        self.resize(screen.width(), screen.height() - 70)
        self.setWindowTitle("共享运维工具集V1.0-czq")

        # self.child2 = ChildrenForm2()

    def createAction(self, text, icon=None, checkable=False, slot=None, tip=None, shortcut=None):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(icon))
        if checkable:
            action.setCheckable(True)  # 可切换
            if slot is not None: action.toggled.connect(slot)
        else:
            if slot is not None: action.triggered.connect(slot)
        if tip is not None:
            action.setToolTip(tip)  # 工具栏提示
            action.setStatusTip(tip)  # 状态栏提示
        if shortcut is not None:
            action.setShortcut(shortcut)  # 快捷键

        return action

    def createFileActions(self):  # 创建文件相关动作

        # 动作分隔符
        self.fileNewAction = self.createAction("&基础工具", icon="filenew.png", checkable=False,
                                               slot=self.fileNew, tip="新建文件", shortcut=QKeySequence.New)
        self.separator = QAction(self)
        self.separator.setSeparator(True)
        self.exitAction = self.createAction("&退出", icon="", checkable=False,
                                            slot=self.close, tip="退出", shortcut=QKeySequence.Close)

    def fileNew(self):

        #QW = QWidget()
        # aa=Ui_MainWindow()
        # aa.setupUi()# 将子页面添加到对应控件QW变量

        # SE =  MainForm1()#本类中窗体

        SE =  SwitchMainForm()#自定义单独文件子窗体

        window = MdiSubWindow()  # 实例化多文档界面对象
        window.setWidget(SE)  # 设置sub内部部件
        window.resize(700,800)
        window.setWindowTitle('核弹 %d' % len(self.mdi.subWindowList()))  # 设置新建子窗口的标题
        # print(sub.windowTitle())
        self.mdi.addSubWindow(window)  # 将子窗口添加到Mdi区域
        window.show()  # 子窗口显示

    def updateWindowMenu(self):  # 动态显示窗口菜单
        self.windowMenu.clear()  # 先清空已有的菜单项
        self.windowMenu.addAction('瀑布排列')
        self.windowMenu.addAction('平铺排列')
        self.windowMenu.addAction("Previous Window")
        self.windowMenu.addAction("Next Window")
        self.windowMenu.addSeparator()

        for window in self.mdi.subWindowList():
            action = self.windowMenu.addAction(window.windowTitle())
            action.setData(window)  # 关联窗口和action

        self.windowMenu.addSeparator()
        self.windowMenu.addAction("关闭激活窗口")
        self.windowMenu.addAction("关闭所有窗口")

        # 点击QAction绑定自定义的槽函数（传递有值【QAction】）
        self.windowMenu.triggered[QAction].connect(self.windowAction)

    def windowAction(self, q):
        if q.text() == '瀑布排列':
            self.mdi.cascadeSubWindows()  # 层叠显示
        elif q.text() == '平铺排列':
            self.mdi.tileSubWindows()  # 平铺显示
        elif q.text() == "Previous Window":
            self.mdi.activatePreviousSubWindow()
        elif q.text() == "Next Window":
            self.mdi.activateNextSubWindow()
        elif q.text() == "关闭激活窗口":
            self.mdi.closeActiveSubWindow()
        elif q.text() == "关闭所有窗口":
            self.mdi.closeAllSubWindows()
        else:  # 激活窗口
            self.mdi.setActiveSubWindow(q.data())
        '''
        currentSubWindow(...)00
        setDocumentMode(self, bool)
        activateNextSubWindow(...)
        activatePreviousSubWindow(...)
        activeSubWindow(...)
        closeAllSubWindows(...)
        closeActiveSubWindow(...)
        removeSubWindow(self, QWidget)
        setActiveSubWindow(self, QMdiSubWindow)
        subWindowList(...)
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mdi = MainWindow()
    mdi.show()
    sys.exit(app.exec_())