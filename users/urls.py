"""define urls for users"""
from django.urls import path
from django.contrib.auth.views import LoginView
from .import views


app_name = 'users'

urlpatterns = [
    # login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # logout page
    path('logout/', views.logout_view, name='logout'),
    # registration page
    path('register/', views.register, name='register'),
]
