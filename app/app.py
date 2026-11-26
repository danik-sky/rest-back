from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from models import Task as db_task
from bp_tasks import bp as bp_task

app = Flask(__name__)
app.config['SECRET_KEY']="Oh no, Cisco Packet Tracer"
app.register_blueprint(bp_task)

class TasksForm(FlaskForm):
    task_name = StringField("Название задачи", validators=[DataRequired(message="Введите название")])
    submit_task = SubmitField("Создать задачу")

if __name__ == "__main__":
    app.run(debug=True)