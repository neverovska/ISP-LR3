from django.contrib.auth.models import User
from django.db import models

from mybakery.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    item = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=0, default=0)
