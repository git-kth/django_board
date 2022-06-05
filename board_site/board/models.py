from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Board(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    view = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board ,on_delete=models.CASCADE, null=True)
    contents = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
