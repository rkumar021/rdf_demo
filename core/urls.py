from django.urls import path,include
from core.views import BookViewSet
from .import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/books',include(router.urls)),
    path('',views.Home,name='home'),
    path('signup/',views.Signup,name='signup'),
    path('login/',views.Login,name='login')

]

#
