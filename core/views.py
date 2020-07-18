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

def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username, email, password1, password2)

        if len(username) < 2 or len(email) < 3:
            messages.error(request, 'Please fill the form correctly')
        else:
            signup = SignUp(username=username, email=email,
                              password1=password1, password2=password2)
            signup.save()
            messages.success(
                request, 'Your message has been successfully sent')
    return render(request,'signup.html')

def Login(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        Signup = authenticate(username=loginusername,password1=loginpassword)

        if Signup is not None:
            login(request,Signup)
            messages.success(request,"successfully Logged In")
            return redirect('home')
        else:
            messages.error(request ,'Invalid Credentials, Please try again')
            return redirect('home')

    else:
        return HttpResponse('404 - Not Found')