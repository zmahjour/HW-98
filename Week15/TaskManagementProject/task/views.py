from django.shortcuts import render
from task.models import Task


def home(request):
    tasks = Task.objects.all().order_by("-id")[0:5]
    return render(request, "home.html", {"tasks": tasks})


def search(request):
    pass


def task_detail(request):
    return render(request, "task_detail.html", context=task)


def all_tasks(request):
    return render(request, "all_tasks.html", context=tasks)
