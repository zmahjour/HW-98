from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Tag(models.Model):
    label = models.CharField(max_length=20)


class Task(models.Model):
    NOT_STARTED = "Not started"
    IN_PROGRESS = "In progress"
    COMPLETED = "Completed"
    STATUS_CHOICES = [
        (NOT_STARTED, "Not started"),
        (IN_PROGRESS, "In progress"),
        (COMPLETED, "Completed"),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=NOT_STARTED
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    tags = models.ManyToManyField(Tag)
