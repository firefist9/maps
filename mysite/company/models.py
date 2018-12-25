from django.db import models

class Company(models.Model):
    name = models.CharField(max_length = 100)
    latitude = models.CharField(max_length = 100)
    longitude = models.CharField(max_length = 100)