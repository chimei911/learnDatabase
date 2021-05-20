import pyodbc

cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 Unicode Driver};SERVER=localhost;DATABASE=test;UID=root;PWD=123456')

cursor = cnxn.cursor()

cursor.execute("select id, name from users")

row = cursor.fetchone()

print('name:', row[1])
print('name:', row.id)
