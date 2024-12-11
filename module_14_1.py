import sqlite3


connection = sqlite3.Connection('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

"""for i in range(1, 11):
    cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?) ', (f'User{i}', f'example{i}@gmail.com', 10*i, 1000))
"""

"""for i in range(1, 11, 2):
    cursor.execute(' UPDATE Users SET balance = ? WHERE id = ? ', (500, i))"""

"""for i in range(1, 11, 3):
    cursor.execute(' DElETE FROM Users WHERE id = ? ', (i,))"""

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()

for i in users:
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')



connection.commit()
connection.close()