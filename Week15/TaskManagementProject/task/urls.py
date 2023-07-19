from django.urls import path
from task import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("detail/<int:pk>/", views.task_detail, name="task_detail"),
    path("all/", views.all_tasks, name="all_tasks"),
]
