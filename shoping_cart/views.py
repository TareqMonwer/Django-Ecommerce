from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from accounts.models import Profile
from products_app.models import Product
from shoping_cart.models import Order, OrderItem




def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.orders.all():
        message = "You already own this ebook"
        return redirect(reverse('products:shop'))
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.save()

    # show confirmation message and redirect back to the same page
    message = "item added to cart"
    return redirect(reverse('products:shop'))
