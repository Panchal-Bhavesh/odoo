from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pet', 'start_date', 'end_date', 'special_requirements']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['facility', 'booking', 'confirmed']
