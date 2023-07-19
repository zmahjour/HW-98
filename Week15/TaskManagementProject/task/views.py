from django.shortcuts import render


def home(request):
    return render(request, "home.html", context=tasks)


def search(request):
    pass


def task_detail(request):
    return render(request, "task_detail.html", context=task)


def all_tasks(request):
    return render(request, "all_tasks.html", context=tasks)
