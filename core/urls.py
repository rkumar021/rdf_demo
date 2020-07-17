from django.urls import path,include
from core.views import BookViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/books',include(router.urls))
]

#
