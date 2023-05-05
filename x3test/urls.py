from django.urls import path

from . import views

urlpatterns = [
    path("th/", views.thirdTest, name="thirdTest"),
    path("testhome/",views.geeks_view,name="testhome"),
    path("testhome/test", views.testing, name="test")

]