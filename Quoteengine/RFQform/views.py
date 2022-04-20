from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def Login(request):
    if request.method=='POST':
        selection=request.POST.get('tool')        
        if selection=='Holemaking':
            return redirect('Holemaking')
        elif selection=='SCEndmill':
            return redirect("SCEndmill")
        elif selection=='Turning':
            return redirect("Turning")
        elif selection=='Milling':
            return redirect("Milling")
        elif selection=='Systems':
            return redirect("Systems")
        else:
            return render(request,"Login.html")
    else:
        return render(request,"Login.html")
   

def Holemaking(request):
    if request.method=='POST':
        selection=request.POST.get('tool')
        if selection=='SCdrill':
            return redirect('SCdrill')
        else:
            return redirect("Systems")
    else:
        return render(request,"Holemaking.html")

def SCEndmill(request):
    return render(request,"SCEndmill.html")

def Milling(request):
    return render(request,"Milling.html")

def Turning(request):
    return render(request,"Turning.html")

def Systems(request):
    return render(request,"Systems.html")

def SCdrill(request):
    return render(request,"Scd.html")
