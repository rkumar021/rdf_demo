from django.contrib import admin
from .models import Book, Signup

# Register your models here.
from . models import Book

admin.site.register(Book)
admin.site.register(Signup)

