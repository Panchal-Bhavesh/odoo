from django.db import models
from django.conf import settings

class Pet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    medical_history = models.TextField(blank=True)
    vaccinations = models.TextField(blank=True)
    dietary_preferences = models.TextField(blank=True)

    def __str__(self):
        return self.name
