import logging

from django.views.generic import ListView, DetailView

from .models import Product

logger = logging.getLogger('main')


class ProductList(ListView):
    logger.info("List of all products")
    model = Product
    template_name = 'bakery/product/list.html'
    context_object_name = 'products'


class ViewProduct(DetailView):
    logger.info("View of one product")
    model = Product
    template_name = 'bakery/product/detail.html'
    context_object_name = 'product'

