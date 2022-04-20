from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import kmt
from django.contrib import messages
import pymongo
from pymongo import MongoClient
from pymongo.read_preferences import ReadPreference
# Create your views here.

#myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
#mydb = myclient["servers"]
#mycol=mydb["KMT"]

def Login(request):
    print("login")
    if request.method=='POST': 
        server=request.POST['Server']
        location=request.POST['Location']
        contact=request.POST['Contact']
        path=request.POST['Path']

        #return redirect('output')
    else:
        return render(request,"findserver.html")
    

def output(request):
    #context={}
    #context['dataset']=KMT.objects.all()
    server1=kmt.objects.all()
    print(server1)
    return render(request,"kmtservers.html",{'destserver':server1})