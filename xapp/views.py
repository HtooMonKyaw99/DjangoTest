from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.
def geeks_view(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "home.html")
def home2(request):
    return render(request,"home1.html")

def nist(request):
    return HttpResponse("Hello ! I'm a django tester begineer!!!!")
def add(request):
    return HttpResponse(3+4)


# Create your views here.
