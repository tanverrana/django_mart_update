from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.store),
    path('product_detail/', views.product_detail),
]
