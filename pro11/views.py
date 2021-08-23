from django.shortcuts import render

def home(request):
    return render(request,"home.html",context={'data':"venugopal"})

def login(request,data1):
    return render(request,"login.html",{"data1":data1})