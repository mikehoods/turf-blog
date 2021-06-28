from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignupForm
from django.urls import reverse_lazy
from .models import Profile

class UserSignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

class EditProfileView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    fields = '__all__'

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'
    
