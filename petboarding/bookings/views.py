from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')


def manage_facilities(request):
    facilities = Facility.objects.all()
    return render(request, 'bookings/manage_facilities.html', {'facilities': facilities})

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'bookings/create_reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'bookings/reservation_success.html')


def payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        token = request.POST['stripeToken']
        amount = int(booking.get_total_cost() * 100)  # amount in cents

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description=f'Booking {booking.id}',
                source=token,
            )
            Payment.objects.create(
                booking=booking,
                stripe_charge_id=charge.id,
                amount=booking.get_total_cost(),
                paid=True,
            )
            booking.confirmed = True
            booking.save()
            return redirect('payment_success')
        except stripe.error.StripeError:
            return render(request, 'bookings/payment_failed.html')
    else:
        return render(request, 'bookings/payment.html', {
            'booking': booking,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
        })

def payment_success(request):
    return render(request, 'bookings/payment_success.html')
