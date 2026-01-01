from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "home/signup.html"
    success_url = reverse_lazy("login")


class LogoutViewInterface(LogoutView):
    template_name = 'home/logout.html'

class LoginViewInterface(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
     template_name = 'home/welcome.html'
     extra_context = {'today': datetime.utcnow(),
                      'title': 'Welcome Home'
                      }


class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin/'



