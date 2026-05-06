from django.urls import path, include
from .views import get_products

urlpatterns = [
    path('', get_products),
    
]