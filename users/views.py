from django.shortcuts import render
#importamos formulario para darse de alta:
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm() #instancia de la clase
    return render(request, 'users/register.html', {'form': form}) #arg: request, template, context