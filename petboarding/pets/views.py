from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm

def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('pet_success')
    else:
        form = PetForm()
    return render(request, 'pets/create_pet.html', {'form': form})

def pet_success(request):
    return render(request, 'pets/pet_success.html')
