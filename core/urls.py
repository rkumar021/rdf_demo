from django.urls import path
from core.views import BookList, Bookcreate, Bookupdatedestroy

urlpatterns = [
    path('api/books',BookList.as_view()),
    path('api/books/new', Bookcreate.as_view()),
    path('api/books/<int:id>', Bookupdatedestroy.as_view())
]

#
