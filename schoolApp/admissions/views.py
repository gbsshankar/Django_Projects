from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def admission(request):
    return HttpResponse( "Hello! admissions")

def admissionreport(request):
    return HttpResponse("Hello! report")