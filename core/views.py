# from django.shortcuts import render
# from rest_framework import Listview
# from rest_framework import serializers
from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
#from rest_framework.response import Response

from core.models import Book
from core.serializers import BookSerializer
# Create your views here.

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Bookcreate(CreateAPIView):
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs ):
        return super().create(request, *args, **kwargs)

class Bookdestroy(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs ):
        return super().delete(request, *args, **kwargs)
        #if response.status_code == 204
        #     from django.core.cache import cache
        #     cache.delete(Book_data)