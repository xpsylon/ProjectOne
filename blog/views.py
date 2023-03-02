from django.shortcuts import render
from django.http import HttpResponse
#importamos la clase Post de blog/models.py:
from .models import Post

#we start passing 'dummy' posts to the blog-home template
#first off we create a list with dictionaries inside.
#Cada diccionario contiene 4 elementos:
posts = [ #lista
    {
        'author': 'Javier La Porte', #diccionario, clave:valor str:str
        'title': 'Blog Post One',
        'content': 'First post content',
        'date_posted': '24 de Febrero, 2023'
    },
    {
        'author': 'Asia Bartczak',
        'title': 'Blog Post Two',
        'content': 'Second post content',
        'date_posted': '24 de Febrero, 2023'
    }
]

def home(request):
    #Now we create a second dictionary using the dictionaries (contents) of the list as values:
    #context = {'posts': posts} #clave:valor para el diccionario context
    #y pasamos este diccionario como tercer argumento al render para pasarlo a home.html:
    #el titulo no esta entre los argumentos, o sea que home.html toma el titulo por default
    
    #en vez de lo de arriba, le pasamos la data de la clase Post guardada en la database:
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)
    #return HttpResponse('<h1>Blog Home</h1>')
    #a view will return wether an HttpResponse or an exception

def about(request):
    return render(request, 'blog/about.html', {'title': 'Kasumi!'})
