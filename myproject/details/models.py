# details/models.py
from django.db import models

class Detail(models.Model):
    movie = models.CharField(max_length=100)
    theatre = models.CharField(max_length=100)

    def __str__(self):
        return self.movie

