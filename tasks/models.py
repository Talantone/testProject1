from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):        #Model for Tasks of users
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=255)

    STATUS = (
        ('u', 'unfinished'),
        ('f', 'finished'),
    )

    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='u', help_text='Task status')


