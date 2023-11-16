from django.urls import path
from . import views

urlpatterns = [
    path('',  views.login, name='loginUser'),
    path('add', views.registartion, name='addUser')
]
#/user/