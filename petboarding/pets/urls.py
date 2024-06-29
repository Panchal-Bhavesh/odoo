from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_pet, name='create_pet'),
    path('success/', views.pet_success, name='pet_success'),
]
