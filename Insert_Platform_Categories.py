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

categories = [{'id': 1, 'name': 'console'}, {'id': 2, 'name': 'arcade'},
              {'id': 3, 'name': 'platform'}, {'id': 4, 'name': 'operating_system'},
              {'id': 5, 'name': 'portable_console'}, {'id': 6, 'name': 'computer'}]


for i in categories:
    cursor.execute('INSERT INTO platform_categories (id, category) VALUES ({id}, "{category}")'
                   .format(id=i.get('id'), category=i.get('name')))

mydb.commit()
