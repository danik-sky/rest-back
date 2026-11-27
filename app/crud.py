import sqlite3

def create_task(name, priority, deadline=None):
    con = sqlite3.connect("example.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO tasks (title, priority, deadline) VALUES (?, ?, ?)", (name, priority, deadline))
    con.commit()
    con.close()

def get_all_tasks():
    con = sqlite3.connect("example.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    result = []
    for task in tasks:
        result.append(list(task))
    con.close()
    return result

def task_done(id):
    con = sqlite3.connect("example.db")
    cursor = con.cursor()
    cursor.execute("UPDATE tasks SET is_done = 1 WHERE id = (?)", (id, ))
    con.commit()
    con.close()

def task_delete(id):
    con = sqlite3.connect("example.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = (?)", (id, ))
    con.commit()
    con.close()

def sort_by_date():
    con = sqlite3.connect("example.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks_sorted (id INTEGER PRIMARY KEY, title TEXT NOT NULL, priority TEXT NOT NULL, deadline TEXT, is_done INTEGER DEFAULT 0)")
    cursor.execute("INSERT INTO tasks_sorted (title, priority, deadline, is_done) SELECT title, priority, deadline, is_done FROM tasks ORDER BY NULLIF(deadline, '') IS NULL, deadline ASC")
    cursor.execute("DROP TABLE tasks")
    cursor.execute("ALTER TABLE tasks_sorted RENAME TO tasks")
    con.commit()
    con.close()

def sort_by_priority():
    con = sqlite3.connect("example.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks_sorted (id INTEGER PRIMARY KEY, title TEXT NOT NULL, priority TEXT NOT NULL, deadline TEXT, is_done INTEGER DEFAULT 0)")
    cursor.execute("INSERT INTO tasks_sorted (title, priority, deadline, is_done) SELECT title, priority, deadline, is_done FROM tasks ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 ELSE 3 END ASC")
    cursor.execute("DROP TABLE tasks")
    cursor.execute("ALTER TABLE tasks_sorted RENAME TO tasks")
    con.commit()
    con.close()