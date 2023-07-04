from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Animal
from .models import Customer
from .models import Locate
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from .forms import MeasurementModelForm

# Create your views here.
def splash(request):
    return render(request, 'splash.html')
    
@login_required(login_url = 'register')
def home(request):
    animal = Animal.objects.all()
    current_time = datetime.now().time().strftime("%H:%M:%S")
    current_date = datetime.today().date()
    return render (request, 'homepage.html', 
    {'current_date':current_date, 'current_time':current_time,'animal':animal})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Customer.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('register')
            elif Customer.objects.filter(email=email).exists():
                messages.error(request, 'Email taken')
                return redirect('register')
            else:
                # the following data will be saved in auth_users
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save(),

                # the following data will be saved in  Customer table
                user_details = Customer.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,)
                user_details.save()

                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.error(request,'password dont match')
        return redirect('register')
    else:    
        return render(request, 'registration.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid details')
            return redirect('login')

    else:   
        return render(request, 'login.html')
    

def link(request):
    return render(request, 'link.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def delete(request,id):
    animal = Animal.objects.get(id=id)
    if request.method == 'POST':
        animal.delete()
        return redirect('home')
        
    return render(request, 'delete.html',{"animal":animal})


# def distance(request):
#     obj = get_object_or_404(Locate, id=1)
#     form = MeasurementModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.destination = form.cleaned_data.get('destination')
#         instance.location = 'Rongo'
#         instance.distance = 500.00
#         instance.save()

#     context = {
#         'distance' : obj,
#         'form' : form,
#     }

#     return render(request, 'location.html', context)