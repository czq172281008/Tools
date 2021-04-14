from PyQt5.QtWidgets import QWidget
from UI.ChildrenForm import Ui_Form

class RightEn(QWidget, Ui_Form):
    def __init__(self):
        super(RightEn, self).__init__()

        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)