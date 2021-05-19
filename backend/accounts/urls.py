from django.urls import path

from accounts.views import CustomUserView, LogoutView, ProfileView

urlpatterns = [
    path('info/', CustomUserView.as_view(), name='user_info'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('profile/', ProfileView.as_view(), name='user_profile'),
]
