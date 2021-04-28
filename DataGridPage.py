import sys
import re
from math import ceil

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QApplication, QPushButton, QLineEdit, QLabel, QSplitter,
                             QTableView, QHeaderView, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
import DB.DBConn as Con
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'#处理结果集乱码


class DataGrid(QWidget):
    isConnected=False
    def __init__(self):#def __init__(self, ip,port,user,password,sname,OrcConStr):
        # self.Ora_ip=ip
        # self.Ora_port=port
        # self.Ora_user=user
        # self.Ora_password=password
        # self.Ora_sname=sname
        # self.OrcConStr=OrcConStr
        # print(self.OrcConStr.split('/'))
        # print(self.OrcConStr.split('/')[0])
        # print(self.OrcConStr.split('/')[1])
        # print(self.OrcConStr.split('/')[2])
        # print(self.OrcConStr.split('/')[3])
        # print(self.OrcConStr.split('/')[4])

        super().__init__()



        self.setWindowTitle("分页查询")
        self.resize(750, 300)

        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 总数页文本
        self.totalPageLabel = None
        # 当前页文本
        self.currentPageLabel = None
        # 转到页输入框
        self.switchPageLineEdit = None
        # 前一页按钮
        self.prevButton = None
        # 后一页按钮
        self.nextButton = None
        # 转到页按钮
        self.switchPageButton = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecrodCount = 0
        # 每页显示记录数
        self.PageRecordCount = 5

        self.db = None
        self.initUI()

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

    def initUI(self):
        # 创建窗口
        self.createWindow()
        # 设置表格
        self.setTableView()

        # 信号槽连接
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)

    def closeEvent(self, event):
        # 关闭数据库
        self.db.close()

    # 创建窗口
    def createWindow(self):
        # 操作布局
        operatorLayout = QHBoxLayout()
        self.prevButton = QPushButton("前一页")
        self.nextButton = QPushButton("后一页")
        self.switchPageButton = QPushButton("Go")
        self.switchPageLineEdit = QLineEdit()
        self.switchPageLineEdit.setFixedWidth(40)

        switchPage = QLabel("转到第")
        page = QLabel("页")
        operatorLayout.addWidget(self.prevButton)
        operatorLayout.addWidget(self.nextButton)
        operatorLayout.addWidget(switchPage)
        operatorLayout.addWidget(self.switchPageLineEdit)
        operatorLayout.addWidget(page)
        operatorLayout.addWidget(self.switchPageButton)
        operatorLayout.addWidget(QSplitter())

        # 状态布局
        statusLayout = QHBoxLayout()
        self.totalPageLabel = QLabel()
        self.totalPageLabel.setFixedWidth(70)
        self.currentPageLabel = QLabel()
        self.currentPageLabel.setFixedWidth(70)

        self.totalRecordLabel = QLabel()
        self.totalRecordLabel.setFixedWidth(70)

        statusLayout.addWidget(self.totalPageLabel)
        statusLayout.addWidget(self.currentPageLabel)
        statusLayout.addWidget(QSplitter())
        statusLayout.addWidget(self.totalRecordLabel)

        # 设置表格属性
        self.tableView = QTableView()
        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.setDropIndicatorShown(True);
        self.tableView.horizontalHeader().setSectionsMovable(True);#列移动
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)#手动调节列宽
        # 创建界面
        mainLayout = QVBoxLayout(self);
        mainLayout.addLayout(operatorLayout);
        mainLayout.addWidget(self.tableView);
        mainLayout.addLayout(statusLayout);
        self.setLayout(mainLayout)

    # 设置表格
    def setTableView(self):

        OrcConStr='11.11.48.64/1521/gxcsdb2/cwbase2_9999/gxtest8888'
        self.connectDB(OrcConStr)
        self.paraSql="""
                    SELECT * FROM SYS_MDL_CTN WHERE MDL_ID 
                    =(SELECT F_YWMX FROM SAFWML WHERE F_BH IN 
                    (select F_FWML from sadjall where F_DJBH='BX30111002020121500058'))
                
                """

        #第一种sql传参格式
        # str='0001'
        # sql=sql.format(str)
        #第二种sql传参格式
        # sql = "insert into goods_detail(Url) values ('%s')" %(Url)
        # sql = "UPDATE goods_detail SET productPrice = %s,productName = %s,stock = %s where  url = %s"
        # cursor.execute(sql,(GoodsDetailPrice,NewGoodsName,Stock, NewGoodsUrl))

        self.data = self.con.Query(self.paraSql)
        # cur=self.con.cursor()
        # cur.execute(self.sql)
        # if(len(self.data)>0):
        #     self.model=QStandardItemModel(len(self.data),len(self.data[0]))#设置行列
        #     self.model.setHorizontalHeaderLabels(self.data[0].keys())#设置列名
        #     rowcount = 0
        #     for row in self.data:
        #         itemcount = 0
        #         for item in row.values():
        #             self.model.setItem(rowcount,itemcount,QStandardItem(str(item)))
        #             # self.tableView.item(rowcount,itemcount).setFlags(Qt.ItemIsSelectable)
        #             itemcount = itemcount+1
        #         rowcount=rowcount+1
        #
        #     self.tableView.setModel(self.model)


        # 声明查询模型
        # self.queryModel = QSqlQueryModel(self)
        # 设置当前页
        self.currentPage = 1;
        # 得到总记录数
        self.totalRecrodCount = len(self.data)
        # 得到总页数
        self.totalPage = self.getPageCount()
        # 刷新状态
        self.updateStatus()
        # 设置总页数文本
        self.setTotalPageLabel()
        # 设置总记录数
        self.setTotalRecordLabel()
        #
        # # 记录查询
        self.recordQuery(1)
        # 设置模型
        # self.tableView.setModel(self.queryModel)
        # self.tableView.setModel(self.model)

        print('totalRecrodCount=' + str(self.totalRecrodCount))
        print('totalPage=' + str(self.totalPage))

        # 设置表格表头
        # self.queryModel.setHeaderData(0, Qt.Horizontal, "编号")
        # self.queryModel.setHeaderData(1, Qt.Horizontal, "姓名")
        # self.queryModel.setHeaderData(2, Qt.Horizontal, "性别")
        # self.queryModel.setHeaderData(3, Qt.Horizontal, "年龄")
        # self.queryModel.setHeaderData(4, Qt.Horizontal, "院系")

    # 得到记录数
    def getTotalRecordCount(self):
        self.queryModel.setQuery("""
        select * from student
        """)
        # self.queryModel.setQuery(self.sql)
        rowCount = self.queryModel.rowCount()
        print('rowCount=' + str(rowCount))
        return rowCount

    # 得到页数
    def getPageCount(self):
        if self.totalRecrodCount % self.PageRecordCount == 0:
            return (self.totalRecrodCount / self.PageRecordCount)
        else:
            return ceil((self.totalRecrodCount / self.PageRecordCount))#向上取整数

    # 记录查询
    def recordQuery(self, page):
        szQuery = ("""
                SELECT * FROM (SELECT embodySQL.*, ROWNUM beginROWNUM
                          FROM (SELECT * FROM SYS_MDL_CTN t WHERE MDL_ID 
                                    =(SELECT F_YWMX FROM SAFWML WHERE F_BH IN 
                                    (select F_FWML from sadjall where F_DJBH='BX30111002020121500058')))  embodySQL
                         WHERE ROWNUM <= %d)
                 WHERE beginROWNUM >= %d
        """ % (page*self.PageRecordCount, (page*self.PageRecordCount-self.PageRecordCount)+1))
        print('query sql=' + szQuery)
        self.data = self.con.Query(szQuery)
        # cur=self.con.cursor()
        # cur.execute(self.sql)
        if(len(self.data)>0):
            self.model=QStandardItemModel(len(self.data),len(self.data[0]))#设置行列
            self.model.setHorizontalHeaderLabels(self.data[0].keys())#设置列名
            rowcount = 0
            for row in self.data:
                itemcount = 0
                for item in row.values():
                    self.model.setItem(rowcount,itemcount,QStandardItem(str(item)))
                    # self.tableView.item(rowcount,itemcount).setFlags(Qt.ItemIsSelectable)
                    itemcount = itemcount+1
                rowcount=rowcount+1

            self.tableView.setModel(self.model)

    # 刷新状态
    def updateStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.currentPageLabel.setText(szCurrentText)

        # 设置按钮是否可用
        if self.currentPage == 1:
            self.prevButton.setEnabled(False)
            self.nextButton.setEnabled(True)
        elif self.currentPage == self.totalPage:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(True)

    # 设置总数页文本
    def setTotalPageLabel(self):
        szPageCountText = ("总共%d页" % self.totalPage)
        self.totalPageLabel.setText(szPageCountText)

    # 设置总记录数
    def setTotalRecordLabel(self):
        szTotalRecordText = ("共%d条" % self.totalRecrodCount)
        print('*** setTotalRecordLabel szTotalRecordText=' + szTotalRecordText)
        self.totalRecordLabel.setText(szTotalRecordText)

    # 前一页按钮按下
    def onPrevButtonClick(self):
        print('*** onPrevButtonClick ');
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(self.currentPage-1)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextButtonClick(self):
        print('*** onNextButtonClick ');
        # if(self.currentPage!=1):
        #     limitIndex = self.currentPage * self.PageRecordCount
        # else:
        self.recordQuery(self.currentPage+1)
        # self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 转到页按钮按下
    def onSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.switchPageLineEdit.text()
        # 判断正整数的正则表达式
        pattern = re.compile('^[1-9]\d*$')
        match = pattern.match(szText)

        # 判断是否为数字
        if not match:
            QMessageBox.information(self, "提示", "请输入数字")
            return

        # 是否为空
        if szText == '':
            QMessageBox.information(self, "提示", "请输入跳转页面")
            return

        # 得到页数
        pageIndex = int(szText)
        # 判断是否有指定页
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        # limitIndex = (pageIndex - 1) * self.PageRecordCount

        # 记录查询
        self.recordQuery(pageIndex);
        # 设置当前页
        self.currentPage = pageIndex
        # 刷新状态
        self.updateStatus();


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口
    example = DataGrid()
    # 显示窗口
    example.show()

    sys.exit(app.exec_())