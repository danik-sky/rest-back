from flask import Blueprint, render_template
from app import TasksForm

bp = Blueprint("tasks", __name__)

@bp.route("/tasks", methods=["GET", "POST"])
def tasks():
    form = TasksForm()
    if form.validate_on_submit():
        name = form.task_name.data
        form.task_name.data = ""
    return render_template("Tasks.html")