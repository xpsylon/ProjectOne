from django.shortcuts import render
from django.http import HttpResponse
#importamos la clase Post de blog/models.py:
from .models import Post

def home(request):
    #en vez de lo de arriba, le pasamos la data de la clase Post guardada en la database:
    context = {'posts': Post.objects.all()} 
    return render(request, 'blog/home.html', context)
   
def about(request):
    return render(request, 'blog/about.html', {'title': 'Kasumi!'}) #argumentos siempre: request, template, context (diccionario)
