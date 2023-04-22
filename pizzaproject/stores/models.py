from django.db import models

# Create your models here.


class Pizzeria(models.Model):
    pizzeria_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)

