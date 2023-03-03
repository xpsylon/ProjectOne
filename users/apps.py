from django.apps import AppConfig
#we need to add this configuration to the project settings.py file
#clase de la clase padre AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
