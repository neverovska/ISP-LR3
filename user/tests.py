from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from user.views import LoginView, RegisterView


class TestURLUser(SimpleTestCase):
    def test_login_url(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_reg_url(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, RegisterView)
