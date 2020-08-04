from django.shortcuts import render, redirect
from rest_framework import serializers
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from core.models import Book, Signup
from core.serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def Home(request):
    allposts = Book.objects.all()
    contaxt = {'allposts':allposts}
    return render(request,'Home.html',contaxt)