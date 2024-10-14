from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    location = models.TextField()

    def __str__(self) -> str:
        return self.name
    

class Employe(models.Model):
    emp_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.emp_name