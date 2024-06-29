from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'age', 'medical_history', 'vaccinations', 'dietary_preferences']
