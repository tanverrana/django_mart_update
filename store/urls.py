from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/',
         views.store, name='products_by_category'),
    path('product_detail/', views.product_detail, name='product_detail'),
]
