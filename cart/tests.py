from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from cart.views import UsersCart


class TestURLCart(SimpleTestCase):
    def test_cart_url(self):
        url = reverse('cart_detail')
        self.assertEquals(resolve(url).func.view_class, UsersCart)
