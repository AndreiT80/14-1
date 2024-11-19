# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

import sqlite3

connection = sqlite3.connect("not_telegram.db")
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

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

'''Заполняем базу 10 записями:'''

for i in range(1, 10):
    cursor.execute( "INSERT INTO Users(username, email, age, balance) VALUES (?,?,?,?)", (f"newuser{i}", f"example{i}@gmail.com", f"{10 * i}", "1000"))

'''Обновляем balance у каждой 2ой записи начиная с 1ой на 500:'''

for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        cursor.execute("UPDATE Users SET balance = ? WHERE Username = ?", ("500", f"newuser{i}"))

'''Удаляем каждую 3ую запись в таблице начиная с 1ой:'''

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

'''Делаем выборку всех записей при помощи fetchall(), где возраст не равен 60 и выводим их
   в консоль в следующем формате (без id):
   Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>'''

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for data in users:
    print(f" Имя: {data[1]} | Почта: {data[2]} | Возраст: {data[3]} | Баланс: {data[4]}")


connection.commit()
connection.close()
