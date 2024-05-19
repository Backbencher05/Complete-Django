from django.db import models

# Create your models here.

class Movie(models.Model):
    Release_date = models.DateField()
    movie_name = models.CharField(max_length=60)
    hero = models.CharField(max_length=50)
    heroine = models.CharField(max_length=50)
    rating = models.FloatField()