from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Board(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    view = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_user')
    like = models.ManyToManyField(User, related_name='like_user')
    unlike = models.ManyToManyField(User, related_name='unlike_user')

    def __str__(self) -> str:
        return self.title

    class Meta:
        permissions = (("manager", "manager on site"),)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board ,on_delete=models.CASCADE, null=True)
    contents = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
