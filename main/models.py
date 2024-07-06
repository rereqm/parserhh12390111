from django.db import models, connection


class Vacancy(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=60)
    url = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    grafic = models.CharField(max_length=40)
    experience = models.CharField(max_length= 40)
    requirement = models.CharField(max_length=3000)
    responsibility = models.CharField(max_length= 3000)
