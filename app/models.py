import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, priority TEXT NOT NULL, deadline TEXT, is_done INTEGER DEFAULT 0)")
conn.commit()
conn.close()
