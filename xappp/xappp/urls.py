from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="logintest"),
    path('login/logintest',views.logintest,name='logintest'),
    path('login/secondlogin',views.secondlogin,name='secondlogin'),
    path('login/pulldata',views.pulldata,name='pull')

    # path("add/",views.add,name="Add"),
    # path("testhtml/",views.geeks_view,name="greek"),
    # path("home2html/",views.home2,name="home2"),
    # path("testhtml/test",views.testing,name="test")
]

