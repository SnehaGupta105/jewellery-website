from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from .models import Contact

#@login_required(redirect_field_name='/login')

# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #     return redirect(request,'login.html')
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        c = Contact(name=name,phone=phone,email=email,msg=msg)
        c.save()
        return redirect('/contact')
    data = Contact.objects.all() #list of all objects
    return render(request,'contact.html',{'data':data})

def catalogue(request):
    return render(request,'catalogue.html')

def loginView(request):       
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
    # A backend authenticated the credentials
            return redirect('/home')
    
        else:
    # No backend authenticated the credentials
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    
    return render(request,'login.html')

def signupView(request):
    if request.method == 'POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        userName=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            user =  User.objects.create_user(userName,email,password)
            user.first_name=firstName
            user.last_name=lastName
            user.save()
            return redirect('/login')
    return render(request,'signup.html')

def logoutView(request):
    logout(request)
    return redirect('/login')