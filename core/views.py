# from django.shortcuts import render
# from rest_framework import Listview
# from rest_framework import serializers
from rest_framework import serializers
from rest_framework import response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
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

class Bookupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs ):
        response = super().delete(request, *args, **kwargs)
        Book_id = request.data.get('id')
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('Book_data_{}'.format(Book_id))
        return response
    def update(self, request, *args, **kwargs ):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            Book = response.data
            cache.set('Book_data_{}'.format(Book['id']),{
                'created': Book['created'],
                'title': Book['title'],
                'description': Book['description'],
                'price': Book['price'] 
            })
        return response

