from django.shortcuts import render,redirect
from django.http import HttpResponse
from Hotel.models import User,Hotel,Phone_Number
# Create your views here.

def index(request):
    if request.method == "POST":
        telephone = request.POST["phone"]
        namehotel = request.POST["hotelname"]
        classroom = request.POST["classroom"]
        #checkin = request.POST["checkin"]
        checkout = request.POST["checkout"]
        quantity_people = request.POST["quantity_people"]
        priceroom = 500.00
        
        booking = User.objects.create(
            telephone = telephone,
            namehotel = namehotel,
            roomhotel = classroom,
            quantity_people = quantity_people,
            pirec_room = priceroom ,
           # date_checkin = checkin,
            date_checkout = checkout
            
            
        )
        booking.save()
        return redirect("/")
    else:
        return render(request, 'index.html')

def login(request):
    
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        telephone = request.POST["phone"]
        
        add_telephone = Phone_Number.objects.create(
            phone = telephone
        )
        add_telephone.save()
        return redirect("/")
    else:
        return render(request, 'register.html')

def recorded(request):
    return render(request, 'recorded.html')

def mybooking(request):
    return render(request, 'mybooking.html')

def about(request):
    return render(request, 'about.html')

def hotelcoco(request):
    return render(request, 'hotelcoco.html')

def hotelamphwa(request):
    return render(request, 'hotelamphwa.html')

def hotelarong(request):
    return render(request, 'hotelarong.html')

def hotelthegret(request):
    return render(request, 'hotelthegret.html')

def hotelroyal(request):
    return render(request, 'hotelroyal.html')
