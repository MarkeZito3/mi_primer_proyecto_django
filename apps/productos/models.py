from django.db import models

class productos(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=9, decimal_places=2)