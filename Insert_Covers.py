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

cursor.execute('SELECT id, coverid '
               'FROM games')
covers = cursor.fetchall()

for i in covers:
    apiurl = 'https://api-v3.igdb.com/covers/{}?fields=*'.format(i[1])
    page = urllib.request.Request(apiurl, headers={
        'user-key': 'a0ef220532796a92d7d3c3e2be7397a1',
        'User-Agent': 'PostmanRuntime/7.11.0'
    })
    infile = urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1')
    jdata = json.loads(data)
    if jdata:
        url = jdata[0].get('url')
        url = 'https:' + url
        req = urllib.request.Request(url, headers={
            'user-key': 'a0ef220532796a92d7d3c3e2be7397a1',
            'User-Agent': 'PostmanRuntime/7.11.0'
        })
        response = urllib.request.urlopen(req)
        direct = 'mysite/static/gamecovers/{}.jpg'.format(i[0])
        f = open(direct, 'wb')
        f.write(response.read())
        f.close()
