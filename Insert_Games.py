import mysql.connector
import urllib.request
import json
import datetime


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='vg'
)
cursor = mydb.cursor()
jdata={}
i = 1

while i<100:
    url = 'https://api-v3.igdb.com/games/{}?fields=*'.format(i)
    page = urllib.request.Request(url, headers={
        'user-key': 'a0ef220532796a92d7d3c3e2be7397a1',
        'User-Agent': 'PostmanRuntime/7.11.0'
    })
    infile = urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1')
    jdata = json.loads(data)

    if jdata:
        time = datetime.datetime.utcfromtimestamp(jdata[0].get('first_release_date'))
        if not jdata[0].get('total_rating'):
            cursor.execute('INSERT INTO games (id, name, first_release_date, coverid) '
                           'VALUES ({id}, "{name}", "{first_release_date}", {coverid})'
                            .format(
                            id=jdata[0].get('id'),
                            first_release_date=time,
                            name=jdata[0].get('name'),
                            coverid=jdata[0].get('cover')))
        else:
            cursor.execute('INSERT INTO games (id, name, first_release_date, total_rating, '
                           'total_rating_count, coverid) '
                           'VALUES ({id}, "{name}", "{first_release_date}", {total_rating}, '
                           '{total_rating_count}, {coverid})'
                            .format(
                            id=jdata[0].get('id'),
                            first_release_date=time,
                            total_rating=jdata[0].get('total_rating'),
                            total_rating_count =jdata[0].get('total_rating_count'),
                            name=jdata[0].get('name'),
                            coverid=jdata[0].get('cover')))


        print(jdata[0].get('id'))

    i = i + 1

mydb.commit()
