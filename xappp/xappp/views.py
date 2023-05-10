# import json
#
# from django.shortcuts import render
#
#
# def login(request):
#     return render(request, "login.html")
#
#
# def logintest(request):
#     # if request.method=='POST':
#     name = request.POST['name']
#     email = request.POST['email']
#     password = request.POST['password']
#     datainfo = {}
#     datainfo.update({len(datainfo): name})
#     datainfo.update({len(datainfo): email})
#     datainfo.update({len(datainfo): password})
#     json_object = json.dumps(datainfo)
#
#     # Writing to sample.json
#     with open("sample.json", "a") as outfile:
#         outfile.write(json_object)
#     # datainfo.append({'name': name, 'email': email, 'password': password})
#     info = {'name': name, 'email': email, 'password': password}
#
#     return render(request, 'logintest.html', {'info': info})
#
#
# def secondlogin(request):
#     return render(request, 'secondlogin.html')
#
# # Create your views here.
import json, pymongo
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request, "login.html")


dict = {}


def logintest(request):
    # if request.method=='POST':
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']

    dict = {"email": email, "username": name, "password": password}

    connection = pymongo.MongoClient("localhost", 27017)
    database = connection["login_info"]
    collection = database["info"]
    collection.insert_one(dict)

    # f = open('userdb.json', 'w')
    # f.write(json.dumps(dict))
    # f.close()

    # Writing to sample.json
    # with open("sample.json", "a") as outfile:
    #     outfile.write(json_object)
    # # datainfo.append({'name': name, 'email': email, 'password': password})
    info = {'name': name, 'email': email, 'password': password}

    return render(request, 'logintest.html', {'info': info})


def secondlogin(request):
    return render(request, 'secondlogin.html')


def pulldata(request):
    with open('userdb.json') as f:
        data = json.load(f)
        useremail = request.POST['email']
        userpassword = request.POST['password']
        for i in data:
            email = data.get(f'{i}').get('email')
            password = data.get(f'{i}').get('password')
            if useremail == email and userpassword == password:
                return render(request, 'LoginSuccess.html')
            else:
                return render(request, 'login.html')

# Create your views here.
