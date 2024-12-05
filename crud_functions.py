import sqlite3


def initiate_db():
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    initiate_db()
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Users''')
    products = cursor.fetchall()
    print(products)
    connection.close()
    return products

def add_product(title, description, price):
    connection = sqlite3.Connection('Product.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (title, description, price) VALUES('{title}', '{description}', '{price}')")
    connection.commit()
    connection.close()


"""add_product('Спать', 'Можешь сладко слип', 100)
add_product('Быть веселее', 'Веселый гном', 200)
add_product('Кушать', 'Не обляпайся', 300)
add_product('Быть Кирилом', 'Ну тут без слов', 400)"""
