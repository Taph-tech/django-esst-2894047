from django.urls import path

from . import views

urlpatterns = [
     path('home', views.home) # Map the /home URL to the home view
]
