from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignupForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class UserSignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    login_url = '/users/login/'
    success_url = reverse_lazy('home')
    fields = ('bio', 'profile_pic', 'website_url', 'medium_url')

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'
    
