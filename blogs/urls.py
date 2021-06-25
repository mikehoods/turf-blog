from django.urls import path
from .views import HomeView, AddPostView, PostDetailView, EditPostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_post/', AddPostView.as_view(), name='add-post' ),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/edit_post/', EditPostView.as_view(), name='edit-post'),
    path('<int:pk>/delete_post/', DeletePostView.as_view(), name='delete-post'),

]