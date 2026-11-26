import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", ('Пример', 'первый'))
cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", ('Пример', 'второй'))
cursor.execute("SELECT * FROM tasks")
res = cursor.fetchall()
print(res)
conn.commit()
conn.close()