from django.contrib import admin
from task.models import Task, Tag, Category

# Register your models here.
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Category)
