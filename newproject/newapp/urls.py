from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path("",views.home),
    path("new1/",views.newfile1),
    path("next1",views.next1,name='next1')
]
