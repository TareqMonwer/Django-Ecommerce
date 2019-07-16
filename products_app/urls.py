from django.urls import path

from .views import product_list


app_name = 'products'

urlpatterns = [
    path('', product_list, name='shop'),
]
