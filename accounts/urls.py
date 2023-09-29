from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.register),
    path('profile/', views.profile),
    path('login/', views.user_login),
]
