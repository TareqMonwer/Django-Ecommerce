from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an email when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order ID: {order_id}"
    body = f"Dear {order.first_name}, \n \n" \
        f"You have successfully placed an order." \
        f"Your order id is: {order_id}."
    mail_sent = send_mail(subject, body, 'tareqmonwer.dpi@gmail.com',
        [order.email])
    return mail_sent
