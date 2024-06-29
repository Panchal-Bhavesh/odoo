from django.contrib import admin
from .models import Booking, Facility, Reservation

admin.site.register(Booking)
admin.site.register(Facility)
admin.site.register(Reservation)
