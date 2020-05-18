from django.urls import path
from .views import registrationview,loginview
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name= 'users'

urlpatterns = [
    
    path('registration/', registrationview, name='registration'),
    path('login/', loginview, name='loginpage'),

    path('password_reset/', 
    auth_views.PasswordResetView.as_view(success_url = reverse_lazy('user:password_reset_done')), 
    name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

  
]