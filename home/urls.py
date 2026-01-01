from django.urls import path

from . import views

urlpatterns = [
     path('', views.HomeView.as_view(), name='home'), # Map the /home URL to the home view
     #path('authorized', views.AuthorizedView.as_view()), # Map the /authorize URL to the authorize view NOT NEEDED NOW
     path('login' , views.LoginViewInterface.as_view(), name='login'), # Map the /login URL to the login view
     path('logout' , views.LogoutViewInterface.as_view(), name='logout'), # Map the /logout URL to the logout view
     path('signup' , views.SignUpView.as_view(), name='signup'), # Map the /signup URL to the signup view
     
]
