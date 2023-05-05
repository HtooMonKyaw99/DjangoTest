from django.shortcuts import render
from django.http import HttpResponse
def test(request):
    return HttpResponse("Hello ! I'm Htoo Mon Kyaw!!!!")
def geeks_view(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "testhome2.html")
def testing(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        info={'name':name,'email':email,'password':password,'phone':phone}
    return render(request,'test.html',{'info':info})
# Create your views here.


