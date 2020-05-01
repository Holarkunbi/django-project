from django.urls import path
from .views import home,registration,loginview

app_name= 'users'

urlpatterns = [
    path('home/', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', loginview, name='loginpage'),
  
]