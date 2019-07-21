import mysql.connector
import json

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='vg'
)
cursor = mydb.cursor()


class UserGames():

    def newgame(self, userid, gameid):
        cursor.execute('INSERT INTO usergames (userid, gameid) '
                       'VALUES ({userid}, {gameid})'.format(userid=userid, gameid=gameid))
        mydb.commit()

    def getusergamesid(self, userid, gameid):
        cursor.execute('SELECT id '
                       'FROM usergames '
                       'WHERE userid = {userid} AND gameid = {gameid}'
                       .format(userid=userid, gameid=gameid))
        usergameid=cursor.fetchone()
        return usergameid[0]

    def newrating(self, usergamesid, rating):
        cursor.execute('INSERT INTO userratings (usergamesid, rating) '
                       'VALUES({usergamesid}, {rating})'
                       .format(usergamesid=usergamesid, rating=rating))
        mydb.commit()

class Games():
    @staticmethod
    def getid(name):
        cursor.execute('SELECT id '
                       'FROM games '
                       'WHERE name = "{name}"'.format(name=name))
        id = cursor.fetchone()
        realid = id[0]
        return realid
    @staticmethod
    def allgames():
        cursor.execute('SELECT name '
                       'FROM games '
                       'ORDER BY name')
        games = cursor.fetchall()
        jsongames = []
        for i in games:
            jsongame = {'name': i[0]}
            jsongames.append(jsongame)
        return jsongames

    @staticmethod
    def getgamesandratings(userid):
        cursor.execute('SELECT games.name, userratings.rating, games.id '
                       'FROM games '
                       'JOIN usergames ON games.id = usergames.gameid '
                       'LEFT JOIN userratings ON usergames.id = userratings.usergamesid '
                       'WHERE usergames.userid = {id} '
                       'ORDER BY games.name'.format(id=userid))
        gamesandratings = cursor.fetchall()
        jsongamesandratings = []
        for i in gamesandratings:
            jsongamesandrating = {'name': i[0], 'rating': i[1], 'id':i[2]}
            jsongamesandratings.append(jsongamesandrating)
        return jsongamesandratings

    @staticmethod
    def getexisting(userid):
        cursor.execute('SELECT games.name '
                       'FROM games '
                       'JOIN usergames ON usergames.gameid = games.id '
                       'WHERE usergames.userid = {id} '.format(id=userid))
        games = cursor.fetchall()
        jsongames = []
        for i in games:
            jsongame = {'name': i[0]}
            jsongames.append(jsongame)
        return jsongames