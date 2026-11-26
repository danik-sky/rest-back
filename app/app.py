from flask import Flask
from models import Task as db_task

app = Flask(__name__)
DataBase = db_task()
Example = DataBase.Dict()
print(Example)

if __name__ == "__main__":
    app.run(debug=True)