from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=96)
    ceo = models.CharField(max_length=96)


class Employee(models.Model):
    eno = models.IntegerField()
    name = models.CharField(max_length=127)
    salary = models.FloatField()
    company = models.CharField(max_length=64)