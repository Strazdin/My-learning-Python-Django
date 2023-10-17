from jinja2 import Template


# 1. Создайте макроопределение для отображения списка пользователей в HTML-документе. У вас есть список пользователей в переменной users, каждый пользователь представлен в виде словаря с ключами name и email. Используйте цикл for и условие if для отображения пользователей, у которых почта кончается на gmail.com

users = [
    {'name': 'Vlad', 'email': 'vlad@gmail.com'},
    {'name': 'Pavel', 'email': 'pavel@mail.ru'},
    {'name': 'Olga', 'email': 'olga@mail.ru'},
    {'name': 'Ivan', 'email': 'ivan@gmail.com'}
]

html = '''
{%- macro list_user(users) -%}
    <ul>
    {% for u in users -%}
    {% if u.email.endswith("gmail.com") -%}
        <li>{{ u.name }} - {{ u.email }}</li>
    {% endif -%}
    {% endfor -%}
</ul>
{%- endmacro %}
{{ list_user(users) }}
'''

tm = Template(html)
msg = tm.render(users=users)
print(msg)


# 2. Создайте макроопределение для отображения списка продуктов в HTML-документе. У вас есть список продуктов в переменной products, каждый продукт представлен в виде словаря с ключами name и price. Используйте цикл for и условие elif для отображения цены в зависимости от диапазона:
# Если цена меньше 10, то пишем, что продукт доступный
# Если цена меньше 20, то пишем, что продукт имеет среднюю цену
# И если цена больше, то пишем, что продукт дорогой

products = [
    {'name': 'спички', 'price': 2},
    {'name': 'мыло', 'price': 13},
    {'name': 'тарелка', 'price': 32},
    {'name': 'шампунь', 'price': 29}
]

html = '''
{%- macro list_user(prod) -%}
    <ul>
    {% for p in prod -%}
    {% if p.price < 10 -%}
        <li>{{ p.name }} - {{ p.price }}: продукт доступный</li>
    {% elif p.price < 20 -%}
        <li>{{ p.name }} - {{ p.price }}: продукт имеет среднюю цену</li>
    {% else -%}
        <li>{{ p.name }} - {{ p.price }}: продукт дорогой</li>
    {% endif -%}
    {% endfor -%}
</ul>
{%- endmacro %}
{{ list_user(prod) }}
'''

tm = Template(html)
msg = tm.render(prod=products)
print(msg)