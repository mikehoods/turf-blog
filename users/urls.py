from django.urls import path
from .views import UserSignupView, EditProfileView, ShowProfileView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('<int:pk>/edit_profile', EditProfileView.as_view(), name="edit-profile"),
    path('<int:pk>/show_profile', ShowProfileView.as_view(), name="show-profile"),
]