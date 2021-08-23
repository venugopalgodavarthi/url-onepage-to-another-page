from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,"register.html")

def logout(request):
    return render(request,"logout.html")


def index(request, input):
    return render(request,"index.html", context={"input":input})

