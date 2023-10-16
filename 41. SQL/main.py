import sqlite3 as sq

cars = [
    ('Mazda', 23000),
    ('Pejo', 19000),
    ('Запорожец', 2000),
    ('Volvo', 10000),
    ('Subaru', 22000)
]

users = [
    ('Влад', 39, 1),
    ('Иван', 44, 3),
    ('Ольга', 22, 2),
    ('Иван', 29, 4),
    ('Павел', 50, 2),
    ('Валентин', 22, 4)
]

with sq.connect('db.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users ('
                      'user_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                      'name TEXT NOT NULL,'
                      'age INTEGER NOT NULL,'
                      'cars_id INTEGER'
                      ')')
    
    cur.executemany('INSERT INTO users VALUES(NULL, ?, ?, ?)', users)

    cur.execute('SELECT * '
                 'FROM users')
    
    # print(cur.fetchall())
    
with sq.connect('db.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cars ('
                      'cars_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                      'model TEXT NOT NULL,'
                      'price INTEGER NOT NULL'
                      ')')
    
    cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)

    cur.execute('SELECT * '
                 'FROM cars')
    
    # print(cur.fetchall())

with sq.connect('db.db') as con:
    cur = con.cursor()
    cur.execute('SELECT name, age, model '
                'FROM users, cars '
                'WHERE users.cars_id = cars.cars_id ')
    print(cur.fetchall())

with sq.connect('db.db') as con:
    cur = con.cursor()
    cur.execute('SELECT name, model '
                'FROM users, cars '
                'WHERE users.cars_id = cars.cars_id AND users.age > 30 '
                'ORDER BY age DESC ')
    print(cur.fetchall())