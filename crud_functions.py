import sqlite3


def initiate_db():
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    initiate_db()
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Products''')
    products = cursor.fetchall()
    print(products)
    connection.close()
    return products

def add_product(title, description, price):
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Products (title, description, price) VALUES('{title}', '{description}', '{price}')")
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    all_users = cursor.execute(f"SELECT * FROM Users").fetchall()
    print(all_users)
    state = False
    for user in all_users:
        if username in user:
            state = True
            break
    connection.close()
    return state

def add_user(username, email, age):
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES('{username}', '{email}', '{age}', '{1000}')")
    connection.commit()
    connection.close()




initiate_db()

"""add_product('Спать', 'Можешь сладко слип', 100)
add_product('Быть веселее', 'Веселый гном', 200)
add_product('Кушать', 'Не обляпайся', 300)
add_product('Быть Кирилом', 'Ну тут без слов', 400)"""
