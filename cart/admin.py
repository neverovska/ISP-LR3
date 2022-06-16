from django.contrib import admin

# Register your models here.
from cart.models import Order


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'item_id', 'quantity']
