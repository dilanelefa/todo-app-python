from django.db import models

# Create your models here.
class TodoTask(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title