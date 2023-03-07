from django.shortcuts import render, redirect #render incluye el protocolo HTTP. Es una abreviacion del mismo.
#redirect es una funcion para redirigir al  usuario a la pagina que querramos una vez que haya enviado el formulario.
#importamos formulario para darse de alta:
#from django.contrib.auth.forms import UserCreationForm. REEMPLAZADA por UserRegisterForm.
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST) #instancia de la clase formulario. REEMPLAZADA!
        form = UserRegisterForm(request.POST)
        if form.is_valid():
             form.save()#metodo de Django para guardar la data del diccionario en la database.
             username = form.cleaned_data.get('username')
             messages.success(request, f'Acount created for {username}!')
             return redirect('entrar') #name del template del login
    else:
        #form = UserCreationForm() #instancia de la clase. REEMPLAZADA!
        form =  UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) #arg: request, template, context

#metodo para el profile usando login_required como decorador:
@login_required
def profile(request):
    return render(request, 'users/profile.html')