"""ProjectOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views #forma de llamarlo mas clara. se le puede dar el nombre que se quiera.
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', user_views.register, name='alta'),
    path('profile/', user_views.profile, name='perfil'),
    #agregamos la variable template_name como argumento al built-in method as_views para decirle donde debe buscar
    #la ruta del template. Por default buscaria en registration/login.html
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='entrar'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='salir'),
]
"""The line from django.contrib.auth import views as auth_views is a Python import statement commonly 
used in Django web applications.
This line imports the views module from the django.contrib.auth package, which contains views and forms 
related to authentication, such as login, logout, and password reset. The as auth_views portion of the import 
statement renames the views module to auth_views, which allows for more concise code later on.

For example, if you wanted to use Django's built-in LoginView class-based view for handling user authentication, 
you could write auth_views.LoginView.as_view() instead of django.contrib.auth.views.LoginView.as_view().
This makes the code easier to read and write."""