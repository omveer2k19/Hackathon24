from django.db import models

# Create your models here.
class Students(models.Model):
    Female = 'F'
    Male = 'M'
    choices = ((Female, 'Female'), (Male, 'Male'))
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=choices, default=Female)
    objects=models.Manager()