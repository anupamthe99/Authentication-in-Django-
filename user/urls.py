from django.urls import path,include
from .views import register ,home

urlpatterns = [
    path('home/',home,name="home"),
    path('register',register,name="register-user"),
    path('accounts/', include('django.contrib.auth.urls')),
]
