from django.urls import path
from . import views

urlspattern = [
    path('', views.post_list, name='post_list'),
]