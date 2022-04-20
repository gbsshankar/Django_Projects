from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from datetime import datetime

#web scraping

url='https://www.timeanddate.com/weather/'
res=requests.get(url).content

soup=BeautifulSoup(res,'html.parser')

def home(request):
    place=soup.find('span',class_="my-city__city")
    temperature=soup.find('span',class_="my-city__wt")
    date=datetime.now
    return render(request,'index.html',{'city':place.text,'temp':temperature.text,'date':date})
def demo(request):
    return render(request,"index.html")



