from email import message
from django.shortcuts import render,redirect
from tsumitheapp.models import userinformations
from django.contrib import messages
import time
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import  NewUserForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def Home_view (request):
    context = {}
    return render(request,'index.html', context)

def customer_info(request):

    if request.method == 'POST':

        first = request.POST['firstname']
        last = request.POST['lastname']
        addy = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        
       
        new_info = userinformations(first_name=first,last_name=last,address=addy,phone=phone,gender=gender)
        new_info.save()
        
        messages.success(request,"Information has been saved succesffully")
        time.sleep(5)

        return redirect('home')

    return render(request,"select.html")


def login_Form(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                messages.info(request, f"You are now logged in as {username} .")
                return redirect("home")
            else:
                messages.error(request,"Invalid username of password")
        else:
            messages.error(request,"Invalid Username or Password")
    form = AuthenticationForm()
    return render(request,"registrations/login.html", {"form":form})





def logoutUser(request):
    logout(request)
    return redirect('login')




def registrationform(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user  = form.save()
            login(request,user)
            messages.success(request,"Registration  Successful.")
            return redirect("login")
        messages.error(request,"Unsuccessful registrations. Invalid information")
    form = NewUserForm()
    return render(request, 'registrations/signup.html',{'form': form})



def choose(request):


    return render(request,"TSUMI/manual_call.html")