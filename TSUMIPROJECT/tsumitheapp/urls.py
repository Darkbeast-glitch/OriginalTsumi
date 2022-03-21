from django.urls import path
from .views import Home_view,customer_info, login_Form,registrationform,logoutUser, choose
urlpatterns = [
    path('', Home_view, name="home"),
    path('info/', customer_info, name="info"),
    path('login/', login_Form, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('signup/', registrationform, name="signup"),
    path('choose/', choose, name="choose"),

    
   
]
