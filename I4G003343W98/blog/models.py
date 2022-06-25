from turtle import title
from django.db import models


class BlogApp(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def _str_(self):
        return self.title