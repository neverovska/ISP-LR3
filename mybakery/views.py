from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from cart.forms import CartAddProductForm
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'bakery/product/list.html'
    context_object_name = 'products'


# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#     return render(request, 'bakery/product/list.html',
#                   {
#                       'category': category,
#                       'categories': categories,
#                   })
#
#
# class CatList(ListView):
#     model = Category
#     template_name = 'bakery/product/list.html'
#     context_object_name = 'categories'
#
#
# class ProductByCat(ListView):
#     model = Product
#     template_name = 'bakery/product/list.html'
#     context_object_name = 'products'
#
#     def get_queryset(self):
#         return Product.objects.filter(category__slug=self.kwargs['category_slug'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c = Category.objects.get(slug=self.kwargs['category_slug'])
#         c_def = self.get_user_context(title='Category - ' + str(c.name),
#                                       cat_selected=c.pk)
#         return dict(list(context.items()) + list(c_def.items()))
# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'bakery/product/list.html',
#                   {
#                       'category': category,
#                       'categories': categories,
#                       'products': products
#                   })

class ViewProduct(DetailView):
    model = Product
    template_name = 'bakery/product/detail.html'
    context_object_name = 'product'




# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug)
#cart_product_form = CartAddProductForm()

#     return render(request, 'bakery/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
