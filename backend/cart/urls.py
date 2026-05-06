from django.urls import path
from .views import add_to_cart, get_cart, update_cart, remove_from_cart

urlpatterns = [
    path('add/', add_to_cart),
    path('', get_cart),
    path('update/', update_cart),
    path('remove/', remove_from_cart),
]