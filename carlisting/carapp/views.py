from django.shortcuts import render, redirect
from .forms import CarForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import BuyForm
from .models import Car
from decimal import Decimal


def buy_form(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            buyer_name = form.cleaned_data['buyer_name']
            buyer_mobile = form.cleaned_data['buyer_mobile']

            # Send email to karan@example.org with the required details
            send_mail(
                'Car Sale Details',
                f'Details of the vehicle: {car.make} {car.model} {car.year}\n'
                f'Details of the seller: {car.seller_name} ({car.seller_mobile})\n'
                f'Sale price: {car.asking_price}\n'
                f'Interested party: {buyer_name} ({buyer_mobile})',
                'anuragbhargava34@gmail.com',
                ['anuragbhargava78@gmail.com'],
                fail_silently=False,
            )

            # Perform calculations for commission and net amount
            # commission = car.asking_price * 0.05
            # net_amount = car.asking_price - commission

            commission = Decimal('1000.00')
            commission_float = float(commission)  # Convert Decimal to float
            percentage = 0.05
            net_amount = commission_float * percentage

            # Update the car status and save it
            car.is_sold = True
            car.save()

            # Redirect to the success page
            return redirect('success', car_id=car_id)

    else:
        form = BuyForm()

    return render(request, 'buy_form.html', {'form': form, 'car': car})


def success_page(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'success.html', {'car': car})

# def car_list(request):
#     # Get filter parameters from the request
#     make = request.GET.get('make')
#     year = request.GET.get('year')

#     # Filter cars based on filter parameters
#     cars = Car.objects.all()
#     if make:
#         cars = cars.filter(make=make)
#     if year:
#         cars = cars.filter(year=year)

#     # Order cars by most recently listed
#     cars = cars.order_by('-id')

#     # Pagination
#     paginator = Paginator(cars, 10)  # 10 cars per page
#     page = request.GET.get('page')

#     try:
#         cars = paginator.page(page)
#     except PageNotAnInteger:
#         cars = paginator.page(1)
#     except EmptyPage:
#         cars = paginator.page(paginator.num_pages)

#     return render(request, 'car_list.html', {'cars': cars, 'make': make, 'year': year})




def index(request):
    # Get filter parameters from the request
    make = request.GET.get('make')
    year = request.GET.get('year')

    # Filter cars based on filter parameters
    cars = Car.objects.all()
    if make:
        cars = cars.filter(make=make)
    if year:
        cars = cars.filter(year__year=year)

    # Order cars by most recently listed
    cars = cars.order_by('-id')

    # Pagination
    paginator = Paginator(cars, 10)  # 10 cars per page
    page = request.GET.get('page')

    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    # print(make,"..........")
    if (make == None):
        make = ''

    return render(request, "index.html", {'cars': cars, 'make': make, 'year': year})
def listCar(request):
    return render(request, "list-car.html")

# @login_required(login_url='login')
def car_listing(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('thank_you', car_id=car.id)
    else:
        form = CarForm()
    return render(request, 'car_listing.html', {'form': form})

def thank_you(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'thank_you.html', {'car': car})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'index.html')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
