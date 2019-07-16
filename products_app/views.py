from django.shortcuts import render

from .models import Product
from shoping_cart.models import Order, OrderItem



def product_list(request):
    products = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile,  is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product for product in user_order_items]

    context = {
        'products': products,
        'current_order_products': current_order_products,
    }
    return render(request, 'shop/products.html', context)
