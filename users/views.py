from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import SignupForm
from django.urls import reverse_lazy

class UserSignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')
