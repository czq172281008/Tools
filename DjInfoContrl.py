import sys

from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget
import DjInfo

#继承页面DjInfo.Ui_Form
class ControlCode(QWidget,DjInfo.Ui_Form):
    sendmsg = pyqtSignal(object)

    def __init__(self):
        QWidget.__init__(self)
        DjInfo.Ui_Form.__init__(self)
        self.setupUi(self)
        self.bt_Search.clicked.connect(self.on_save)


    def on_save(self):
        if(self.F_DJBH.text()==''):
            QMessageBox.information(self, "单据编号",
                                self.tr("单据编号为空"))

class BackendThread(QThread):
    Sign = pyqtSignal(object)
    def run(self):
        while True:
            data = DjInfo.Ui_Form()
            self.Sign.emit(data.bt_Search.clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = ControlCode()
    md.show()
    sys.exit(app.exec_())
