from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('manage_facilities/', views.manage_facilities, name='manage_facilities'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('payment/<int:booking_id>/', views.payment, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
]
