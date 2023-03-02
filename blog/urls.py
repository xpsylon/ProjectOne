from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #va a ser reenviado desde el urls.py principal
    path('about/', views.about, name='blog-about'),
]