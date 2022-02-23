import mysql.connector

cnx = mysql.connector.connect(user = 'root', 
password = 'mnMySQL2022',
host = '127.0.0.1',
database = 'Farm',
auth_plugin = 'mysql_native_password'
)

cursor = cnx.cursor()
query = ('SELECT * FROM Customers')
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

#cleanup
cursor.close()
cnx.close