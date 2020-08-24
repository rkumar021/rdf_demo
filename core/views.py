from django.shortcuts import render, redirect
from rest_framework import serializers
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from .serializers import CreateUserSerializer

CLIENT_ID = 'xj5wy7roTCYh4MSuyNSCuJJRboHw77yLeMzWtCSi'
CLIENT_SECRET = '9lN1HoruklWYrl8DPKZ4QlLV150UqtKViys1aHbZNyMSVdEiGJwt8pyWxFjco8oWS5ekUBq6RoVuJSwIjio4KWf99CTqVzwRmLQH4eyWw0g2TLUH3qeDzWIIItWhUYmp'

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

def UpdateBook(request,bookid):
    bookid = bookid
    book = Book.objects.filter(id=bookid)
    return render(request, 'updatebook.html', {'book':book[0],'bookid':bookid})

def ShowAllRecord(request):
    return render(request, 'allrecord.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer 
    serializer = CreateUserSerializer(data=request.data) 
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save() 
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/', 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)