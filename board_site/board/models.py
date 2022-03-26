from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    contents = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    view = models.IntegerField()

    def __str__(self) -> str:
        return self.title