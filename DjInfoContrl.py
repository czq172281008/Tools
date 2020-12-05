import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import DjInfo

#继承页面DjInfo.Ui_Form
class ControlCode(QMainWindow, DjInfo.Ui_Form):
    def __init__(self):
        QMainWindow.__init__(self)
        DjInfo.Ui_Form.__init__(self)
        self.setupUi(self)
        self.bt_Search.clicked.connect(self.on_save)
        #self.btn_open.clicked.connect(self.on_open)

    def on_save(self):
        FullFileName, _ = QFileDialog.getSaveFileName(self, '文件另存为', r'./', 'TXT (*.txt)')
        set_text = self.txt_view.toPlainText()
        with open(FullFileName, 'wt') as f:
            print(set_text, file=f)

    def on_open(self):
        txtstr = ""
        FullFileName, _ = QFileDialog.getOpenFileName(self, '打开', r'./', 'TXT (*.txt)')
        with open(FullFileName, 'rt') as f:
            lines = f.readlines()
            for line in lines:
                txtstr = txtstr + line
        self.txt_view.setText(txtstr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = ControlCode()
    md.show()
    sys.exit(app.exec_())
