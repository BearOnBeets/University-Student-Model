from django.db import models

# Create your models here.
from django.db import models

class University(models.Model):
    university_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class Student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    grade=models.CharField(max_length=1)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

