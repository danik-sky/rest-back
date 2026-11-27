from flask import Blueprint, render_template, url_for, redirect, request
from forms import TasksForm
from datetime import datetime
from crud import *

bp = Blueprint("tasks", __name__)

@bp.route("/tasks", methods=["GET", "POST"])
def tasks():
    form = TasksForm()
    message = ''
    if request.method == "POST":
        if form.validate_on_submit() and form.submit_task.data:
            return redirect(url_for("tasks.create"), code=307)
        for name in request.form:
            if "done" in name:
                id = int(name.split("_")[1])
                return redirect(url_for("tasks.task_is_done", id=id), code=307)
            elif "delete" in name:
                id = int(name.split("_")[1])
                return redirect(url_for("tasks.task_is_delete", id=id), code=307)
            elif "date" in name:
                return redirect(url_for("tasks.sort_date"), code=307)
            elif "priority" in name:
                return redirect(url_for("tasks.sort_priority"), code=307)
    all_tasks = get_all_tasks()
    return render_template("Tasks.html", form=form, message=message, tasks=all_tasks)

@bp.route("/create", methods=["POST"])
def create():
    form = TasksForm()
    name = form.task_name.data
    if (not isinstance(name, str)) or (name.strip()==""):
        message = 'Неккоректное имя пользователя'
        form.task_name.data = ""
        return render_template("Tasks.html", form=form, message=message)
    priority = form.priority.data
    deadline = form.deadline.data
    form.task_name.data = ""
    create_task(name, priority, deadline)
    return redirect(url_for("tasks.tasks"))

@bp.route("/tasks/<int:id>/done", methods=["POST"])
def task_is_done(id):
    task_done(id)
    return redirect(url_for("tasks.tasks"))

@bp.route("/tasks/<int:id>/delete", methods=["POST"])
def task_is_delete(id):
    task_delete(id)
    return redirect(url_for("tasks.tasks"))

@bp.route("/tasks/sort/date", methods=["POST"])
def sort_date():
    sort_by_date()
    return redirect(url_for("tasks.tasks"))

@bp.route("/tasks/sort/priority", methods=["POST"])
def sort_priority():
    sort_by_priority()
    return redirect(url_for("tasks.tasks"))