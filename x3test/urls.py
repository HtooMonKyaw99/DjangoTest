from django.urls import path

from . import views

urlpatterns = [
    path("th/", views.thirdTest, name="thirdTest"),
]