from django.contrib.auth.models import User
from django.db import models

from mybakery.models import Product


class Order(models.Model):
    owner_name = models.CharField(max_length=100, db_index=True,  default='')
    item_id = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    quantity = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    name = models.CharField(max_length=100, db_index=True, default='')
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    @classmethod
    def create(cls, owner_name, item_id, quantity, name, image, price):
        order = cls(owner_name=owner_name, item_id=item_id, quantity=quantity, name=name, image=image, price=price)
        return order

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


    def __str__(self):
        return self.owner_name