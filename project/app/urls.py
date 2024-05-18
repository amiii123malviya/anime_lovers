from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('contact/',contact,name='contact'),
    path('registerdata/',registerdata,name='registerdata'),
    path('explore/',explore,name='explore'),


]