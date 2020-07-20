from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

class Signup(models.Model):
    Role = (
    ("Supervisor", "SV"),
    ("Teachers", "T"),
)
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE, max_length=150)
    email = models.EmailField()
    password1 = models.CharField(max_length=25)
    password2 = models.CharField(max_length=25)
    usertype = models.CharField(choices=Role, max_length=50)


    def __str__(self):
        return self.username
     