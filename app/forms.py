from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TasksForm(FlaskForm):
    task_name = StringField("Название задачи", validators=[DataRequired(message="Введите название")])
    submit_task = SubmitField("Создать задачу")