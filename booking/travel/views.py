from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import credentials
from . import serializers
from . import models
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
# Create your views here.

def login(request): 
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['passw']                
        user1=credentials.objects.filter(user_name=username, pass_word=password)
        print(user1)
        if user1.exists():            
            return redirect("index")
        else:
            messages.success(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"login.html")

def home(request):
    pass

def index(request):
    if request.method=="POST":
        customer_name=request.POST['customername']
        customer_mobile=request.POST['customermobile']
        customer_comments=request.POST['customercomment']
        print(customer_name)
        print(customer_mobile)
        print(customer_comments)
        send_mail("Booking customer feedback","customername: "+customer_name+" "+"customermobile: "+customer_mobile+" "+"customercomment: "+customer_comments,"kennatesting42@gmail.com",["kennatesting42@gmail.com"])        
        messages.info(request,"We will get in touch with you!!!")        
        return render(request,"index.html")
    else:
        return render(request,"index.html")

def register(request):    
    if request.method=="POST":        
        username=request.POST['user']
        password=request.POST['passw']
        emailid=request.POST['email']        
        user1=credentials.objects.filter(user_name=username)
        emailid1=credentials.objects.filter(email=emailid)
        if user1.exists():
            messages.info(request,"User already exists")
        elif emailid1.exists():
            messages.info(request,"Email already exists")
        else:
            credentials.objects.create(user_name=username,pass_word=password,email=emailid).save()
            messages.info(request,"User created successfully")
            print("data inserted successfully!!!")

        #queryset=models.credentials.objects.all()
        #serializer_class= serializers.CredentialsSerializer        
        return redirect("login")
    else:        
        return render(request,"register.html")









