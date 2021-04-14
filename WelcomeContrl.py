from PyQt5.QtWidgets import QWidget
from UI.Welcome import *

class WelContrl(QWidget, Ui_WelForm):
    def __init__(self):
        super(WelContrl, self).__init__()

        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)