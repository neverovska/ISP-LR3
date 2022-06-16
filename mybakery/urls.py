from django.urls import path
from . import views
from .views import ProductList, ViewProduct

app_name = 'mybakery'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:id>/<slug:slug>', ViewProduct.as_view(),
         name='product_detail')
]