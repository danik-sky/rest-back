from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired

class TasksForm(FlaskForm):
    task_name = StringField("Название задачи ", validators=[DataRequired(message="Введите название")])
    priority = SelectField("Приоритет задачи", choices=[
            ('low', 'Низкий'),
            ('medium', 'Средний'),
            ('high', 'Высокий')
        ] ,validators=[DataRequired(message="Выберите приоритет")])
    deadline = DateField("Дата конца задачи")
    submit_task = SubmitField("Создать задачу")
    done = SubmitField("Выполнить")
    delete = SubmitField("Удалить")