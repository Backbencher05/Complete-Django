from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60)
    marks = models.IntegerField()
    roll_no = models.IntegerField()
    