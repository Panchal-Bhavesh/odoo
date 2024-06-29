from django.db import models
from django.conf import settings
from pets.models import Pet
import stripe

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    special_requirements = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.pet.name} ({self.start_date} to {self.end_date})"


class Facility(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.facility.name} - {self.booking}"
    


class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.booking} - {self.amount} - {self.paid}"

