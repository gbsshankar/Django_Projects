from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import win32com.client as client
# Create your views here.

def sum(request):
    if request.method=='POST':        
        a=int(request.POST['num1'])
        b=int(request.POST['num2'])
        res=a+b 
        return render(request,'sum.html',{'result':res})
    else:
        return render(request,'sum.html')



def email(request):    
    try:
        send_mail("RFQ Form", "This email generated from rfq", "bhavani.sankar@kennametal.com", ['bhavani.sankar@kennametal.com'])
    except:
        return HttpResponse('Make sure all fields are entered and valid.')

    #if request.method=='POST':        
        #try:
            #send_mail("RFQ Form", "This email generated from rfq", "bhavani.sankar@kennametal.com", ['bhavani.sankar@kennametal.com'])
        #except BadHeaderError:
            #return HttpResponse('Invalid header found.')
        #return HttpResponseRedirect('/contact/thanks/')
    #else:
        # In reality we'd use a form class
        # to get proper validation errors.
        #return HttpResponse('Make sure all fields are entered and valid.')