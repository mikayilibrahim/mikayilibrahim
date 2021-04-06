from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages




# Create your views here.

#register
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username =form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.info(request, "qeydiyatdan keçdiniz")
        return redirect("index")
    context = {"form":form}
    return render(request, "reglog/register.html",context)
    
   

#login
def loginUser(request):
    form = LoginForm(request.POST or None)
    context= {'form':form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"istifadəçi adı və ya parol səfdir")
            return render(request,"reglog/login.html",context)
       
        messages.success(request,"xoş gəldiniz")
        login(request, user)
        return redirect("index")
    return render(request, "reglog/login.html",context)    
#logout
def logoutUser(request):
    logout(request)
    messages.success(request,"çıxış etdiniz !")
    return redirect("index")
    

