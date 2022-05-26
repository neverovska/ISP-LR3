from django.urls import reverse

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mybakery:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    weight = models.DecimalField(max_digits=5, decimal_places=0)
    calories = models.DecimalField(max_digits=5, decimal_places=1)
    composition = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mybakery:product_detail', args=[self.id, self.slug])
