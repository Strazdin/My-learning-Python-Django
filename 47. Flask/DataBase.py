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
            self.__cur.execute('SELECT id, username, name, content, time FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res:
                return res 
        except IOError:
            print('Ошибка чтения базы данных')
        return []
    
    def get_post(self, post_id):
        try:
            self.__cur.execute(f'SELECT username, name, content, time FROM posts WHERE id == {post_id}')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из базы данных' + str(e))
        return None, None

    def add_post(self, username, name, content):
        try:
            tm = int(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)', (username, name, content, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных' + str(e))
            return False
        return True
    
    def add_comment(self, name, comment, post_id):
        try:
            tm = int(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)', (name, comment, tm, post_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных' + str(e))
            return False
        return True
    
    def get_comments(self, post_id):
        try:
            self.__cur.execute(f'SELECT * FROM comments WHERE post_id == {post_id}')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из базы данных' + str(e))
        return None, None







