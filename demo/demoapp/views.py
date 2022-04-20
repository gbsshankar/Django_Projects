from django.shortcuts import (get_object_or_404,render, HttpResponseRedirect)
from django.http import HttpResponse
from .models import demomodel
from .forms import demoform

# Create your views here.
def create(request):
    # dictionary for initial data with field names as keys
    context ={}
    form=demoform(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,"create_view.html",context)

def list_view(request):
    context={}
    context['dataset']=demomodel.objects.all()
    return render(request,"list_view.html",context)

def detail_view(request,id):
    context={}
    context['data']=demomodel.objects.get(id=id)
    return render(request,"detail_view.html",context)

def update_view(request,id):
    context={}
    obj=get_object_or_404(demomodel,id=id)
    form=demoform(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"]=form
    return render(request,"update_view.html",context)

def delete_view(request,id):
    context={}
    obj=get_object_or_404(demomodel,id=id)
    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"delete_view.html",context)



