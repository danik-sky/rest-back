import sqlite3

conn = sqlite3.connect("example.db")

class Task():
    cursor = conn.cursor()
    dict = {"id": [], "title": [], "priority": [], "deadline": [], "is_done": []}
    cursor.execute("SELECT * FROM tasks")
    for task in cursor.fetchall():
        dict["id"].append(task[0])
        dict["title"].append(task[1])
        dict["priority"].append(task[2])
        dict["deadline"].append(task[3])
        dict["is_done"].append(task[4])
    def Dict(self):
        return self.dict