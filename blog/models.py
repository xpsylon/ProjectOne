from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#The main built-in class is Model in models module:

#the class Post will be a table stored in the migrations directory after running the python manage.py makemigration command.
#File is migrations/0001_initial.py
class Post(models.Model): #post will be the table of a database.
    title = models.CharField(max_length=100) #title is a table field, model is module and CharField is a class
    content = models.TextField() #text field is text with no restrictions
    date_posted = models.DateTimeField(default=timezone.now) #we dont put timezone.now(), just timezone.now because we dont
    #want to execute the now function, but just to set it as a default value.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #ForeignKey is the ID of each table how I understand it.
    """ This line of code defines a foreign key relationship between the `Post` model and the `User` model in Django. A foreign key is a field in one table that refers to the primary key of another table. In this case, the `author` field in the `Post` model is a foreign key that refers to the `id` field in the `User` model. This means that each post is associated with a single user who created it.

    The `on_delete` argument specifies what should happen when the referenced object (in this case, a `User` object) is deleted. `models.CASCADE` is a built-in Django option that specifies that when a `User` object is deleted, all of the `Post` objects associated with that `User` should also be deleted."""

    #agregamos metodo double underscore __str__ para customizar
    #el output de los posts:
    def __str__(self) -> str:
        return self.title