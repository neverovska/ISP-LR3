from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from mybakery.views import ProductList


class TestURLMyBakery(SimpleTestCase):
    def test_user_url(self):
        url = reverse('product_list')
        self.assertEquals(resolve(url).func.view_class, ProductList)
