# DebS 

import cx_Oracle
from typing import List

#constring = cx_Oracle.makedsn("localhost", "1521", "O12CR201")

class DB:
    def __init__(self,ip,port,sid,user, password):
        #self.constring = cx_Oracle.makedsn(ip, port, sid) #makedsn服务名带01无效必须用这种形式dsn='11.11.48.64:1521/gxbxorcl01'
        self.constring = ip+':'+port+'/'+sid
        self.password = password
        self.user = user

    def Connect(self):
        self.con = cx_Oracle.connect(user=self.user, password=self.password, dsn=self.constring)
        print('Oracle版本' + self.con.version)
        print("连接成功！")
        self.cursor = self.con.cursor()

    def Version(self):
        return self.con.version

    def Query(self, query)-> List[dict]:
        self.cursor.execute(query)
        colnames = list(map(lambda x: x.lower(), [d[0] for d in self.cursor.description]))
        rows = self.cursor.fetchall()
        result = [dict(zip(colnames, row)) for row in rows]
        return result
    
    
    
    def TablesSearch(self, owner:str, search:str)-> [str]:
        try:
            #print(search)
            def innerfunc(owner:str, searchstr:str)->List[str]:
                percentile:str = "%"
                searchstr = percentile.__add__(searchstr).__add__(percentile)
                #SELECT table_name FROM dba_tables WHERE upper(owner)=upper('cwbase2_9999') and upper(table_name) like upper('%saxclb%') ORDER BY table_name
                tbquery = ''' SELECT table_name FROM dba_tables WHERE upper(owner)=upper(:1) and upper(table_name) like upper(:2) ORDER BY table_name'''
                self.cursor.execute(tbquery, (owner,searchstr))
                rows = list(self.cursor.fetchall())
                return rows
            tableslist = innerfunc(owner,search)
            res = []
            for name in tableslist:
                res.append(name.__getitem__(0))
            return res

        except Exception as e:
            self.cursor.close()
            self.con.close()
            print('执行失败！%s'%e)


    def TablesWithColumnName(self, owner:str, search:str)->[str]:
        # print(search)
        def innerfunc(owner:str,colname:str)-> List[str]:
            tbquery = '''select table_name from all_tab_columns where upper(owner)=upper(:1) and upper(column_name) = upper(:2) and TABLE_NAME not like 'KEY_%' and  TABLE_NAME not like 'V_%' '''
            self.cursor = self.con.cursor()
            self.cursor.execute(tbquery,(owner,colname))
            rows = list(self.cursor.fetchall())
            return rows
        tableslist = innerfunc(owner, search)
        res = []
        for name in tableslist:
            res.append(name.__getitem__(0))
        return res
    
    def GetDistValue(self, column:str, table:str)->[str]:
        def innerfunc(owner:str,colname:str)-> List[str]:
            query = ' select distinct '+column+' from '+table+' order by '+column+' asc '
            
            self.cursor = self.con.cursor()
            self.cursor.execute(query)
            rows = list(self.cursor.fetchall())
            return rows
        tableslist = innerfunc(column, table)
        res = []
        for name in tableslist:
            res.append(str(name.__getitem__(0)))
        #print(res)
        return res
 
    def GetAllColumns(self, table)-> List[dict]:
        query = ''' select COLUMN_NAME , data_type , data_length  from ALL_TAB_COLUMNS where upper(TABLE_NAME)=upper(:1) and upper(data_type) in ( upper('varchar2'), upper('varchar')) '''
        self.cursor.execute(query,  (table,))
        colnames = list(map(lambda x: x, [d[0] for d in self.cursor.description]))
        rows = self.cursor.fetchall()
        result = [dict(zip(colnames, row)) for row in rows]
        return result

    def GetAllColumnsForTable(self, table)-> List[dict]:
        query = ''' select COLUMN_NAME as "Column Name" , data_type as "Data Type", data_length  as "Max Length"  from ALL_TAB_COLUMNS where upper(TABLE_NAME)=upper(:1) '''
        self.cursor.execute(query,  (table,))
        colnames = list(map(lambda x: x, [d[0] for d in self.cursor.description]))
        rows = self.cursor.fetchall()
        result = [dict(zip(colnames, row)) for row in rows]
        return result

    def Close(self):
        self.cursor.close()
        self.con.close()
        print('析构了')

    # def __del__(self):
    #     self.cursor.close()
    #     self.con.close()
    #     print('析构了')

