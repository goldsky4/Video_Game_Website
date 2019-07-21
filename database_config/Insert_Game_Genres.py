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
jdata={}
i = 1

while i<101:
    url = 'https://api-v3.igdb.com/games/{}?fields=*'.format(i)
    page = urllib.request.Request(url, headers={
        'user-key': 'a0ef220532796a92d7d3c3e2be7397a1',
        'User-Agent': 'PostmanRuntime/7.11.0'
    })
    infile = urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1')
    jdata = json.loads(data)
    if jdata:
        for y in jdata[0].get('genres'):
            cursor.execute('INSERT INTO game_genres (game_id, genre_id) '
                           'VALUES ({game_id}, {genre_id})'
                .format(
                game_id=jdata[0].get('id'),
                genre_id=y))


            print(jdata[0].get('id'))

    i = i + 1

mydb.commit()
