from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Name: {self.name}"


class Tag(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return f"Label: {self.label}"


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
    created = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=NOT_STARTED
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return (
            f"Task: {self.title} | Due date: {self.due_date} | Status: {self.status} "
        )
