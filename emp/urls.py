from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('viewemp',views.viewemp,name='views'),
    path('addemp',views.addemp,name='add'),
    path('delemp',views.delemp,name='del'),
    path('filteremp',views.filteremp,name='filter'),
    # path('filteremp',views.filteremp,name='filter1')
]