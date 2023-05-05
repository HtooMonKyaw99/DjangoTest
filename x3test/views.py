from django.shortcuts import render
from django.http import HttpResponse
def thirdTest(request):
    return HttpResponse("Hello ! I'm third tester!!!")
def testing(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        info={'name':name,'email':email,'password':password,'phone':phone}
    return render(request,'test.html',{'info':info})
def geeks_view(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "home.html")
# Create your views here.



# Create your views here.
