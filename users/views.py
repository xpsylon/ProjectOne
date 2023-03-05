from django.shortcuts import render, redirect #render incluye el protocolo HTTP. Es una abreviacion del mismo.
#redirect es una funcion para redirigir al  usuario a la pagina que querramos una vez que haya enviado el formulario.
#importamos formulario para darse de alta:
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
             username = form.cleaned_data.get('username')
             messages.success(request, f'Acount created for {username}!')
             return redirect('blog-home') #name de la home de blog en blog/urls.py
    else:
        form = UserCreationForm() #instancia de la clase
    return render(request, 'users/register.html', {'form': form}) #arg: request, template, context