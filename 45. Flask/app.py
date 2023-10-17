from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kpokfkodfjisnfn39i3dsnvn8yy68hjnenr84u8i'

menu = [
    {'name': 'Блог', 'url': '/'},
    {'name': 'Создать тему', 'url': '/create'},
]

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Содержание', menu=menu)

@app.route('/create', methods=['POST', 'GET'])
def contacts():
    if request.method == 'POST':
        if len(request.form['username']) > 1 and len(request.form['name']) > 1 and len(request.form['content']) > 1:
            flash('Сообщение отправлено успешно!', category='success')
            context = {
            'username': request.form['username'],
            'name': request.form['name'],
            'content': request.form['content'],
            }
            return render_template('create.html', **context, title='Создать тему', menu=menu)
        else:
            flash('Ошибка отправки!', category='error')
            
    return render_template('create.html', title='Создать тему', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
