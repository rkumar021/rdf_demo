# from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets

from core.models import Book
from core.serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

