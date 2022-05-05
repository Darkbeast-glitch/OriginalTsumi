from django.urls import path
from .views import Home_view,customer_info, login_Form,registrationform,logoutUser, choose, manual_order,order_manually,order_received,Profile_page,services,Tasker
urlpatterns = [
    path('', Home_view, name="home"),
    path('info/', customer_info, name="info"),
    path('login/', login_Form, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('signup/', registrationform, name="signup"),
    path('choose/', choose, name="choose"),
    path('manualorder/', manual_order, name="manualorder"),
    path('ordermanual/', order_manually, name="ordermanual"),
    path('order_received/', order_received, name="order_received"),
    path('profile_page/', Profile_page, name="profile_page"),
    path('serivces', services, name="services"),
    path('Tasker', Tasker, name="Tasker")
    # path('contact/', contact, name="contact"),

    
   
]
