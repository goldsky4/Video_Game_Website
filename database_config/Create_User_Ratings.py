import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='vg'
)
cursor = mydb.cursor()

cursor.execute('CREATE TABLE userratings (id INT AUTO_INCREMENT PRIMARY KEY, '
               'usergamesid INT,'
               'rating FLOAT)')

