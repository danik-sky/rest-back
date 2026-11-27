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
    return result