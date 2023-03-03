from django.contrib import admin
#importamos la clase Post de models:
from .models import Post
#y creamos una interface para manejar post en la admin site
admin.site.register(Post)
