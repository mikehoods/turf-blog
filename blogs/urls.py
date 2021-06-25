from django.urls import path
from .views import HomeView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_post/', AddPostView.as_view(), name='add-post' ),

]