from email import message
from django.shortcuts import get_object_or_404, render,redirect
from tsumitheapp.models import Contact_form, Payment, userinformations,Tsu_MI_Details,Popular_Details,PaymentFees
from django.contrib import messages
import time
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import  NewUserForm,ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from . import forms
from django.contrib.auth.decorators import login_required




# Create your views here.

def Home_view (request):
    pop_details = Popular_Details.objects.all()

    if request.method == 'POST':
        fullname = request.POST['Fullname']
        email_address = request.POST['email']
        phone = request.POST['phonenumber']
        message = request.POST['message']

        contact_form = Contact_form(fullname=fullname,email=email_address,phone=phone,message=message)
        contact_form.save()
         
        messages.success(request,"Your messages has been sent successfully our representative will reach out to you in a short time 😎")
        time.sleep(5)

    context = {

        'pop_details':pop_details
    }
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

@ login_required(login_url='login')
def choose(request):


    return render(request,"TSUMI/manual_call.html")
@ login_required(login_url='login')
def manual_order(request):


    return render(request, "TSUMI/manualorder.html")

@ login_required(login_url='login')
def order_manually(request):
    
    if request.method == "POST":
        fullname = request.POST['fname']
        city = request.POST['City']
        location = request.POST['location']
        ordertype = request.POST['ordertype']
        category = request.POST['category']
        phonenumber = request.POST['phonenumber']
        itemlist = request.POST['itemlist']
            

        Details = Tsu_MI_Details(fullname=fullname, city=city, address= location, send_type=ordertype,category_name=category, phone_number=phonenumber, item_list=itemlist)
        Details.save()
        return redirect('initiate_payment')
            


    return render(request,"TSUMI/manualorder_real.html")

def order_received(request):
    context = {}
    return render(request, 'TSUMI/order_received.html',context)



# Profile__page
@ login_required(login_url='login')
def Profile_page(request):

    context = {}
    return render(request, "Account/profile_page.html", context)

# services page

def services(request):
    context = {}
    return render(request, 'TSUMI/services.html', context)


# view for taskers
@ login_required(login_url='login')
def Tasker(request):

    context = {
        'Prices':[
            {'Deliveryprice' : 50},
            {'Cleaning' : 150},
            {'Decoration' : 20},
            {'Carwash' : 80},
            {'Deepclean' : 60},
            {'Errands' : 550},
           
        ]
    }
    return render (request, 'TASKER/tasker.html',context)



# Payments
@ login_required(login_url='login')
def initiate_payment(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        details = Tsu_MI_Details.objects.all()
        payment_form = forms.PaymentForm(request.POST)
        payment_fees = PaymentFees.objects.all()
       
        if payment_form.is_valid:
            payment = payment_form.save()
            return render (request,'Payments/make_payment.html', {'payment':payment, 'payment_fees':payment_fees,'details':details, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})

    else:
        payment_form = forms.PaymentForm()
        return render (request,'Payments/initiate_payment.html',{'payment_form':payment_form})


# Verify Payment
@ login_required(login_url='login')
def verify_payment(request:HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()

    if verified:
        messages.success(request, "Verification Successful")
    else:
        messages.error(request, "Verification Failed")
        
    return redirect('initiate_payment')









































































































































































# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			subject = "Website Inquiry" 
# 			body = {
# 			'first_name': form.cleaned_data['first_name'], 
# 			'last_name': form.cleaned_data['last_name'], 
# 			'email': form.cleaned_data['email_address'], 
# 			'message':form.cleaned_data['message'], 
# 			}
# 			message = "\n".join(body.values())

# 			try:
# 				send_mail(subject, message, 'bbjulius900@gmail.com', ['bbjulius900@gmail.com']) 
# 			except BadHeaderError:
# 				return HttpResponse('Invalid header found.')
# 			return redirect ("home`")
      
# 	form = ContactForm()
# 	return render(request, "contact.html", {'form':form})

# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['receiver@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('redirect to a new page')