from django.urls import path

from . import views

urlpatterns = [
    path("nist/", views.test, name="test"),
    #path("add/",views.add,name="add")
    path("testhome2/",views.geeks_view,name="testhome"),
    path("testhome2/test", views.testing, name="test")
]