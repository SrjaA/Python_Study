import random
import sqlite3

# Создаём Базу данных
bd = sqlite3.connect('arithmetic.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
table = bd.cursor()
# Создадим таблицу с двумя текстовыми колонками
table.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
a=random.randint(0,9)
b=random.randint(0,9)
# Заполняем таблицу данными
table.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''',(a,b))
# Сохраняем изменения
bd.commit()

table.execute('''SELECT col_1,col_2 FROM tab_1''')
k = table.fetchall()
print(k)
