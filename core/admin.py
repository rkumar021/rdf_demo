from django.contrib import admin
from .models import Book, User

# Register your models here.
from . models import Book

admin.site.register(Book)
# admin.site.register(Signup)

admin.site.register(User)

