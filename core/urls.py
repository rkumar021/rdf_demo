from django.urls import path
from core.views import BookList

urlpatterns = [
    path('api/books',BookList.as_view()),

]
