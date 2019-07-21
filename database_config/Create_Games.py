import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='vg'
)
cursor = mydb.cursor()

cursor.execute('CREATE TABLE games (id INT AUTO_INCREMENT PRIMARY KEY, '
                                    'name VARCHAR(100)), '
                                    'first_rele')

