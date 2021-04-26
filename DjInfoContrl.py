import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QFrame, QSplitter, \
    QTextEdit

from UI.DjInfo import Ui_Form #单独QTDesigner绘制窗体文件
from DataGridPage import DataGrid
import DB.DBConn as Con
from DataGridPage import *
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'#处理结果集乱码

class ControlCode(QWidget,Ui_Form):#继承QTDesigner绘制窗体文件单独页面DjInfo.Ui_Form实现界面和逻辑分离
    sendmsg = pyqtSignal(object)
    isConnected = False
    Ora_ip = ''
    Ora_port = ''
    Ora_password = ''
    Ora_user = ''
    Ora_sname=''
    OrcConStr=''#11.11.75.13/1521/gxbxorcl01/cwbase2_9999/gxtest8888

    def __init__(self, parent=None):
        super(ControlCode, self).__init__(parent)#可替换成# QWidget.__init__(self) # QWidget.__init__(self)
        # QWidget.__init__(self)
        # QWidget.__init__(self)
        # qb=QTableInfo.BookStorageViewer()
        self.setupUi(self)#初始化DjInfo.Ui_Form

        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        self.DataTable.setVisible(False)
        self.bt_Search.clicked.connect(lambda: self.on_Search())


    def on_Search(self):
        # self.editHost.setText("11.11.48.64")
        # self.editPassword.setText("gxtest8888")
        # self.editPort.setText("1521")
        # self.editSID.setText("gxcsdb2")
        # self.editUser.setText("cwbase2_9999")
        # self.lineEditSearch.setText("saxclb")
        if(self.DB_CS.isChecked()):
            Ora_ip = '11.11.48.64'
            Ora_port = '1521'
            Ora_user = 'cwbase2_9999'
            Ora_password = 'gxtest8888'
            Ora_sname='gxcsdb2'
            OrcConStr='11.11.48.64/1521/gxcsdb2/cwbase2_9999/gxtest8888'

        if(self.F_DJBH.text()!=''):
            self.DataTable.setVisible(False)
            btncont = self.layout.count()
            #widget = QtWidgets.QTableView()
            self.connectDB(OrcConStr)
            sql="SELECT CTN_ID,MDL_ID FROM SYS_MDL_CTN WHERE MDL_ID =(SELECT F_YWMX FROM SAFWML WHERE F_BH IN (select F_FWML from sadjall where F_DJBH='BX30111002020121500058'))"

            #第一种sql传参格式
            # str='0001'
            # sql=sql.format(str)
            #第二种sql传参格式
            # sql = "insert into goods_detail(Url) values ('%s')" %(Url)
            # sql = "UPDATE goods_detail SET productPrice = %s,productName = %s,stock = %s where  url = %s"
            # cursor.execute(sql,(GoodsDetailPrice,NewGoodsName,Stock, NewGoodsUrl))

            data = self.con.Query(sql)
            self.tableView = QTableView()


            rowcount = 0
            for row in data:
                itemcount = 0
                for item in row.values():
                    self.tableView.QStandardItem(rowcount,itemcount,QtWidgets.QTableWidgetItem(str(item)))
                    self.tableView.item(rowcount,itemcount).setFlags(Qt.ItemIsSelectable)
                    itemcount = itemcount+1
                rowcount=rowcount+1

            widget = DataGrid(Ora_ip,Ora_port,Ora_user,Ora_password,Ora_sname,OrcConStr)
            # self.widget.setGeometry(10, 10, 380, 240)
            self.layout.addWidget(widget)
            widget2 = QtWidgets.QTableView()
            self.layout.addWidget(widget2)

            topleft = QFrame()
            topleft.setFrameShape(QFrame.StyledPanel)

            bottom = QFrame()
            bottom.setFrameShape(QFrame.StyledPanel)

            splitter1 = QSplitter()
            textedit = QTextEdit()
            splitter1.addWidget(topleft)
            splitter1.addWidget(textedit)
            splitter1.setSizes([200, 100])

            splitter2 = QSplitter()
            splitter2.addWidget(splitter1)
            splitter2.addWidget(bottom)

            widget2 = QWidget()
            song = QtWidgets.QLabel('难得')
            gridlayout = QtWidgets.QGridLayout()
            gridlayout.addWidget(song, 0, 0)
            widget2.setLayout(gridlayout)

            self.layout.addWidget(splitter2)
            self.layout.addWidget(splitter2)
            self.layout.addWidget(splitter2)
            self.layout.addWidget(widget2)

            # QW1 = QWidget()
            # DjinfoW1 = ttt.Czq()
            #
            # DjinfoW1.setupUi(QW1)  # 将子页面添加到对应控件QW变量
            # gridlayout1 = QtWidgets.QGridLayout()
            # QW1.setLayout(gridlayout1)
            # self.layout.addWidget(QW1)

            # qb = QTableInfo.BookStorageViewer()
            # qb.show()
            # QMessageBox.information(self, '单据编号",
            #                     self.tr("单据编号为空"))

        else:
            self.DataTable.setVisible(True)
            QMessageBox.information(self, "提示",
                                    self.tr("单据编号为空"))


    def Data(self, tablename, sqlcond, table):
        query = 'select * from '
        query+=tablename
        query+= ' '
        rowCount = table.rowCount()
        condlist = []
        for row in range(rowCount):
            colname = table.item(row, 0).text()
            colvalue = table.cellWidget(row,3).currentText()
            coltype  = table.item(row, 1).text()
            if colvalue != "-select-":
                if "VARCHAR" not in coltype:
                    condlist.append(" "+colname+" = "+colvalue+" ")
                else :
                    condlist.append(" "+colname+" = '"+colvalue+"' ")

        if len(condlist) > 0:
            query += " where"
        for i in range(len(condlist)):
            if i > 0:
                query+= sqlcond
            query += condlist[i]

        #query +=" ;" #lol does not take ; wasted  day :-)
        data = self.con.Query(query)
        diag = DataGrid()
        self.resUI = QtWidgets.QWidget()
        diag.setupUi(self.resUI)
        # add data
        diag.setupdata(data,tablename,self,query,self.writer)
        self.resUI.setWindowTitle(tablename+':Data')
        self.resUI.show()
        self.colResUI.append(self.resUI)

    def connectDB(self,strCnn):
        if self.isConnected is False: #是否连接，未连接进行连接
            ip=strCnn.split('/')[0]# OrcConStr='11.11.75.13/1521/gxbxorcl01/cwbase2_9999/gxtest8888'
            port=strCnn.split('/')[1]
            sname=strCnn.split('/')[2]
            username=strCnn.split('/')[3]
            password=strCnn.split('/')[4]

            self.con = Con.DB(ip,port,sname,username,password)
            self.con.Connect()
        else:
            self.con.Close()
        self.isConnected = not self.isConnected

    # self.editHost.setText("11.11.75.13")
    # self.editPassword.setText("gxtest8888")
    # self.editPort.setText("1521")
    # self.editSID.setText("gxbxorcl01")
    # self.editUser.setText("cwbase2_9999")
        # self.editHost.setEnabled(False)
        # editfields = [self.editHost,self.editPassword,self.editPort,self.editSID,self.editUser]
        # if self.isConnected is True:
        #     self.btnConnect.setText("Disconnect")
        #     self.pushSearch.setEnabled(True)
        #     for edit in editfields:
        #         edit.setEnabled(False)
        #
        #     # self.writer.AddLine('Connected to '+self.con.Version(),False)#困扰一天这条语句报错导致界面没有进行更新强制退出
        # else:
        #     self.pushSearch.setEnabled(False)
        #     self.btnConnect.setText("Connect")
        #     for edit in editfields:
        #         edit.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = ControlCode()
    md.show()
    sys.exit(app.exec_())
