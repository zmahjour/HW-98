from django.shortcuts import render
from task.models import Task


def home(request):
    tasks = Task.objects.all().order_by("-id")[0:5]
    return render(request, "home.html", context={"tasks": tasks})


def search(request):
    if request.method == "GET":
        search = request.GET["search"]
        results = Task.objects.filter(
            title__contains=search, tags__label__contains=search
        )
    return render(
        request, "search.html", context={"search": search, "results": results}
    )


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "task_detail.html", context={"task": task})


def all_tasks(request):
    tasks = Task.objects.all().order_by("-id")
    return render(request, "all_tasks.html", context={"tasks": tasks})
