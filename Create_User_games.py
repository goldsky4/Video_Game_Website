import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='vg'
)
cursor = mydb.cursor()

cursor.execute('CREATE TABLE usergames (id INT AUTO_INCREMENT PRIMARY KEY, '
               'userid INT,'
               'gameid INT)')

