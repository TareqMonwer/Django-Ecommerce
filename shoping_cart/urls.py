from django.urls import path

from .views import add_to_cart


app_name = 'cart'


urlpatterns = [
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
]
