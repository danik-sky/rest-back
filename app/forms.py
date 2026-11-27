from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Optional

class TasksForm(FlaskForm):
    task_name = StringField("Название задачи ")
    priority = SelectField("Приоритет задачи ", choices=[
            ('low', 'Низкий'),
            ('medium', 'Средний'),
            ('high', 'Высокий')
        ] ,validators=[DataRequired(message="Выберите приоритет")])
    deadline = DateField("Дата конца задачи ", validators=[Optional()])
    submit_task = SubmitField("Создать задачу")
    done = SubmitField("Выполнить")
    delete = SubmitField("Удалить")
    date_sort = SubmitField("Отсортировать по дате")
    priority_sort = SubmitField("Отсоритровать по приоритету")