from django.urls import path

from . import views

urlpatterns = [
    path("", views.nist, name="nist"),
    path("add/",views.add,name="Add"),
    path("testhtml/",views.geeks_view,name="greek"),
    path("home2html/",views.home2,name="home2")
]