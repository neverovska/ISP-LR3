from django.urls import path
from . import views
from .views import RegisterView, LoginView

app_name = 'user'

urlpatterns = [
    path('', RegisterView.as_view(), name='signup'),
    path('signin', LoginView.as_view(), name='signin'),
]