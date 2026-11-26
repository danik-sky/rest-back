from flask import Blueprint, render_template
from forms import TasksForm
from datetime import datetime
from crud import *

bp = Blueprint("tasks", __name__)

@bp.route("/tasks", methods=["GET", "POST"])
def tasks():
    form = TasksForm()
    message = ''
    if form.validate_on_submit():
        name = form.task_name.data
        if (not isinstance(name, str)) or (name.strip()==""):
            message = 'Неккоректное имя пользователя'
            form.task_name.data = ""
            return render_template("Tasks.html", form=form, message=message)
        priority = form.priority.data
        deadline = form.deadline.data
        form.task_name.data = ""
        create_task(name, priority, deadline)
    return render_template("Tasks.html", form=form, message=message)