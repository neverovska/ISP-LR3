import logging

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from mybakery.models import Product
from .models import Order

logger = logging.getLogger('main')


def cart_add(request, product_id):
    product = Product.objects.get(pk=product_id)
    order = Order.create(request.user.username, product_id, 1, product.name, product.image, product.price)
    order.save()
    return redirect('/')


class UsersCart(LoginRequiredMixin, ListView):
    logger.info("List of all orders")
    model = Order
    template_name = 'cart/detail.html'
    context_object_name = 'order'
    login_url = reverse_lazy('user:signin')
