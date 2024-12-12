from django.shortcuts import render
from .models import Doctor

def home(request):
    return render(request, 'home.html')

def doctors(request):
    doctors_list = Doctor.objects.all()  # Barcha shifokorlarni olish
    return render(request, 'doctor_list.html', {'doctors': doctors_list})

def appointment(request):
    return render(request, 'appointment_form.html')

def register(request):
    return render(request, 'register.html')
