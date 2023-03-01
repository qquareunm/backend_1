from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(null=False, max_length=255, blank = False)
    surname = models.CharField(null=False, max_length=255, blank=False)
    year_of_study = models.IntegerField()

