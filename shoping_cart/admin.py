from django.contrib import admin

from .models import OrderItem, Order


admin.site.register(Order)
admin.site.register(OrderItem)
