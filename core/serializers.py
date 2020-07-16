from rest_framework import serializers
from core.models import Book


class BookSerializer(serializers.Serializer):
    
    class meta:
        model = Book
        fields = "__all__"
    