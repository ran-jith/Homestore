from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    prize = models.IntegerField()
    thump = models.ImageField(default='default.jpeg', blank=True)
    seller = models.ForeignKey(User,default=None)

    def __str__(self):
        return self.name
