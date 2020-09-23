from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
     path("",views.index,name='home'),
     path('digitalsolution',views.digitalsolution,name="digitalsolution")
]