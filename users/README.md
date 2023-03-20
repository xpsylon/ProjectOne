#USER APP STEP BY STEP
1. pyhton manage.py startapp users
2. Add app to settings.py INSTALLED APPS:
   1. Check in users/app: Users.Config
   2. Add users.app Users.Config to INSTALLED APPS
3. create a register view in users/views:
   1. from django.contrib.auth.forms import UserCreationForm
   2. def register(request):
         formulario = UserCreationForm() <!--instancia de la clase-->
4. Create template: users/register.html
   1. {% extends "blog/base.html %}
   2. {% block content %} add div and form html tags and css classes {% endblock content %}
   3. Add the mandatory security to the form: <form>{% csrf_token %}
   4. Add a fieldset and a legend inside the form
   5. Imprimimos el formulario:
      1. {{ form_clave }}. Clave del contexto (diccionario). forma basica
      2. {{ form_clave.as_p }}. Metodo que mejora el output.
   6. Agregamos un boton submit</form>
   7. Agrgamos un div para sign in por si ya tienen una cuenta.
5. Podriamos crear un archivo users/urls.py para el routing, pero vamos a usar el urls.py del Proyecto:
   1. from users import views as users_views
   2. path('register/', user_views.register, name='alta')



