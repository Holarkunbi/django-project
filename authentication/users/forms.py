from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class  RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(
                attrs={'autocomplete': 'new-password',
                        'placeholder':'Enter your password',
                        'class':'form-control'}),
        
    )
    password2 = forms.CharField(
        label= ("Password confirmation"),
        widget=forms.PasswordInput(
                attrs={'autocomplete': 'new-password',
                        'placeholder':"Confirm your password ",
                        'class':'form-control'}),
        strip=False,
        
    )
    last_name = forms.CharField(
        label=("Last Name"),
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 
                        'placeholder':'Enter your first name',
                        'id':'last_name'}
    )   )
    first_name = forms.CharField(
        label=("First Name"),
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Enter your last name'})
    )
    username = forms.CharField(
        label=("Username"),
        max_length=15,
        widget=forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Enter your username'})
    )
    email = forms.CharField(
        label=("Email"),
        max_length=50,
        widget=forms.EmailInput(attrs={'class':'form-control',
        'placeholder':'Enter your Email'})
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']

