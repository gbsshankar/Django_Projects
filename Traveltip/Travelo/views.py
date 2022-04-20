from django.shortcuts import render
from . models import destination
# Create your views here.

def index(request):

    dest1=destination.objects.all()        
    return render(request,"index.html",{'dests':dest1})