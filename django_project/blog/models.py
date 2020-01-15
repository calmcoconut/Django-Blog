"""
models usually inhert from django's model class

"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100) # a character field.
    content = models.TextField(max_length=200) # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now) # Django's time handling class; timezone.now is a
    # function from django's utility modules

    # we need our user now. import user model. One to many relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE) # makes author unique id. on_delete=Cascade means if a
    # user leaves, all their posts will also be deleted

    def __str__(self):
        return self.title

    """to let the create post view redirect, we must supply reverse url"""
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) #this is the detail post primary key