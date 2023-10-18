import sqlite3
import os

from flask import Flask, render_template, request, flash, g, abort

from DataBase import DataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'fd3cacfcf68f607e4dd7a598352b4452138d67bd'

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db 

@app.route('/index')
@app.route('/')
def index():
    db = get_db()
    dbase = DataBase(db)
    return render_template('index.html', title='Блог', menu=dbase.get_menu(), posts=dbase.get_posts())

@app.route('/create', methods=['POST', 'GET'])
def create():
    db = get_db()
    dbase = DataBase(db)

    if request.method == 'POST':
        if len(request.form['username']) > 1 and len(request.form['name']) > 1 and len(request.form['content']) > 1:
            res = dbase.add_post(request.form['username'], request.form['name'], request.form['content'])
            if res:
                flash('Пост добавлен успешно!', category='success')
            else:
                flash('Ошибка добавления поста!', category='error')
        else:
            flash('Ошибка добавления поста!', category='error')
    return render_template('create.html', title='Добавление статьи', menu=dbase.get_menu())

@app.route('/post/<int:post_id>')
def show_post(post_id):
    db = get_db()
    dbase = DataBase(db)

    username, name, content, tm = dbase.get_post(post_id)
    if not name:
        abort(404)

    if request.method == 'POST':
        if len(request.form['name']) > 1 and len(request.form['comment']) > 1:
            res = dbase.add_comment(request.form['name'], request.form['comment'], post_id)
            if res:
                flash('Комментарий добавлен успешно!', category='success')
            else:
                flash('Ошибка добавления комментария!', category='error')
        else:
            flash('Ошибка добавления комментария!', category='error')

    return render_template('post.html', id=post_id, username=username, name=name, content=content, tm=tm, menu=dbase.get_menu(), comments=dbase.get_comments(post_id))


if __name__ == '__main__':
    app.run(debug=True)
