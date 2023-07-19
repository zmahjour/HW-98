from django.urls import path
from .views import home, search, task_detail, all_tasks

urlpatterns = [
    path("home/", views.home, neme="home"),
    path("search/", views.search, name="search"),
    path("detail/<int:id>/", views.task_detail, name="task_detail"),
    path("all/", views.all_tasks, name="all_tasks"),
]
