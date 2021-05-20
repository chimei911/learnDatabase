import pyodbc
 
class DBHelper(object):
 
    def __init__(self, host, port, database, user, password):
        #conn_info = 'Driver={SQL Server};Database=%s;Server=%s,%s;Uid=%s;Pwd=%s' % (dbName, serverIp, port, uid, pwd)
        conn_info = ('Driver={MySQL ODBC 5.3 Unicode Driver};Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'%(host, port, database, user,password))
        self.connection = pyodbc.connect(conn_info, unicode_results=True)
        self.cursor = self.connection.cursor()
 
    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
 
    def destroy(self):
        if self.cursor:
            print(self.cursor, 'destroy cursor closed')
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
 
    # 获取全部查询结果
    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
  
    #获取查询条数
    def count(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]
 
    #执行语句，包括增删改，返回变更数据数量
    def execute(self, sql):
        count = self.cursor.execute(sql).rowcount
        self.connection.commit()
        return count
 
db = DBHelper('localhost',3306,'test','root','123456')
list = db.query('select * from t1 limit 5')
print(list)