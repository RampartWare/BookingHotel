from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def recorded(request):
    return render(request, 'recorded.html')
def mybooking(request):
    return render(request, 'mybooking.html')
def about(request):
    return render(request, 'about.html')
def hotelcoco(request):
    return render(request, 'hotelcoco.html')