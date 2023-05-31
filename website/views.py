from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Customer

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def login_user(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            # messages.success(request, "You have been Logged In!")
            return redirect('dashboard')
        else:
             messages.success(request,"Invalid Credentials!")
             return redirect('login')
    else:
        return render(request,'login_user.html',{})
def dashboard(request):
    customers = Customer.objects.all()
    return render(request,'dashboard.html',{'customers':customers})
def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"All done!")
            return redirect('dashboard')
    else:
        form = SignUpForm()     
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def customer_profile(request,pk):
    if request.user.is_authenticated:
        # Look up Customer's profile
        customer_profile = Customer.objects.get(id=pk)
        return render(request,'customer.html',{'customer_profile':customer_profile})
    else:
        messages.success(request,"You have to login First!")
        return redirect('login')
    
def delete_customer(request,pk):
    if request.user.is_authenticated:
        delete_customer = Customer.objects.get(id=pk)
        delete_customer.delete()
        return redirect('dashboard')
    else:
        messages.success(request,"You have to login First!")
        return redirect('login')
    
def add_customer(request):
    return render(request,'add_customer.html',{})

        