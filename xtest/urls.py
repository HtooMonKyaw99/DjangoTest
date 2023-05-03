from django.urls import path

from . import views

urlpatterns = [
    path("nist/", views.test, name="test"),
    #path("add/",views.add,name="add")
]