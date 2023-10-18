import sqlite3
import time

class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res 
        except IOError:
            print('Ошибка чтения базы данных')
        return []
    
    def get_posts(self):
        sql = 'SELECT * FROM posts'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res 
        except IOError:
            print('Ошибка чтения базы данных')
        return []

    def add_post(self, username, name, content):
        try:
            tm = int(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)', (username, name, content, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных' + str(e))
            return False
        return True






