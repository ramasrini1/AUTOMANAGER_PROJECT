from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer

# Create your views here.
def home(request):
  return render(request, 'management/home.html')

def signupuser(request):
  if request.method == 'GET':
        return render(request, 'management/signupuser.html', {'form': UserCreationForm()})
  else:
      if request.POST['password1'] == request.POST['password2']:
        try:
          user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
          user.save()
          login(request, user)
          return redirect('home')
        except IntegrityError:
          return render(request, 'management/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
      else:
        return render(request, 'management/signupuser.html', {'form':UserCreationForm(),
        'error': 'Passwords did not match'})

def loginuser(request):
  if request.method == 'GET':
        return render(request, 'management/loginuser.html', {'form': AuthenticationForm()})
  else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'management/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
 if(request.method =='POST'):
   logout(request)
   return redirect('home')

@login_required
def dashboard(request):
   return render(request, 'management/dashboard.html')

@login_required
def addcustomer(request):
  if request.method == 'GET':
    return render(request, 'management/addcustomer.html', {'form': CustomerForm()})
  else:
    try: 
      form = CustomerForm(request.POST) 
      print(form['name'].value())
      if form.is_valid():
          print("validForm")
      else:
          print("invalidform")
      newcustomer = form.save(commit=False)
      print("form data saved")
      #newcustomer.user = request.user
      newcustomer.save()
      return redirect('customers')
    except ValueError:
      return render(request, 'management/addcustomer.html', {'form':CustomerForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def customerlist(request):
   customers = Customer.objects.all()
   return render(request, 'management/customerlist.html', {'customers':customers})

@login_required
def customers(request):
   customers = Customer.objects.all()
   return render(request, 'management/customers.html', {'customers':customers})

@login_required
def customer(request, customer_pk):
   #customers = Customer.objects.all()
   customer = get_object_or_404(Customer, pk=customer_pk)
   return render(request, 'management/customer.html', {'customer':customer})

@login_required
def deletecustomer(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')

@login_required
def editcustomer(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == 'GET':
      return render(request, 'management/editcustomer.html', {'customer':customer})
    else:
      try: 
        form = CustomerForm(request.POST, instance=customer) 
        form.save()
        return redirect('customers')
      except ValueError:
        return render(request, 'management/editcustomer.html', {'customer':customer})
    