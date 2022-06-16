from django.contrib import admin
from .models import  Product
from django.utils.safestring import mark_safe



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'weight']
    list_editable = ['price', 'weight']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

        image_show.__name__ = "Картинка"