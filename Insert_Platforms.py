import mysql.connector
import urllib.request
import json

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='vg'
)
cursor = mydb.cursor()


cursor.execute('INSERT INTO test')


mydb.commit()
