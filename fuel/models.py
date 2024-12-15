# fuel/models.py

from django.db import models

class FuelStop(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)  # State abbreviation
    price_per_gallon = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state} - ${self.price_per_gallon:.2f}"
