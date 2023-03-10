from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,"Username has been created successfully")
            return redirect("home")
    else:
        form=UserCreationForm()
    
    return render(request,"register.html",{'form':form})

# @login_required(login_url="register-user")
def home(request):
    return render(request,"home.html")

