from django.shortcuts import render
from django.db.models import Q
from task.models import Task


def home(request):
    tasks = Task.objects.all().order_by("-id")[0:4]
    return render(request, "home.html", {"tasks": tasks})


def search(request):
    if request.method == "GET":
        search = request.GET["search"]
        results = Task.objects.filter(
            Q(title__icontains=search) | Q(tags__label__icontains=search)
        ).distinct()

        return render(request, "search.html", {"search": search, "results": results})


def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, "task_detail.html", {"task": task})


def all_tasks(request):
    tasks = Task.objects.all().order_by("-id")
    return render(request, "all_tasks.html", {"tasks": tasks})
