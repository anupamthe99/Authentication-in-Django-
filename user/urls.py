from django.urls import path
from .views import register ,home

urlpatterns = [
    path('home/',home,name="home"),
    path('register',register,name="register-user")
]
