# from django.shortcuts import render
# from rest_framework import Listview
# from rest_framework import serializers
from rest_framework.generics import ListAPIView
#from rest_framework.response import Response

from core.models import Book
from core.serializers import BookSerializer
# Create your views here.

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
