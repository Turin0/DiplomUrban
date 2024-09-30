from django.db import models
from django.urls import reverse
# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10000, decimal_places=2)
    size = models.DecimalField(max_digits=1000, decimal_places=3)
    description = models.TextField()
    reviews = models.TextField()
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_id': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    reviews = models.TextField()

    def __str__(self):
        return self.title
