from django.contrib.postgres.fields import ArrayField
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    students = ArrayField(models.CharField(max_length = 100), blank = True)
