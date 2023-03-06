#Creamos este archivo para crear una clase que herede de UserCreationForms para poder customizarla y agregarle campos.
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): #inherits from UserCreationForm
    email = forms.EmailField() #and adds an email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
