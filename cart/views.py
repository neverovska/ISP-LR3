
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from mybakery.models import Product
from .models import Order


# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')


#
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')
#
#
# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
#                                                                    'update': True})
#     return render(request, 'cart/detail.html', {'cart': cart})
#
class UsersCart(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'cart/detail.html'
    context_object_name = 'order'


# class NewOrder():


# class Product(LoginRequiredMixin, CreateView):
#     logger.info('Posting Product')
#     form_class = AddProductForm
#     template_name = 'marketplace/post_product.html'
#     login_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super(PostProduct, self).form_valid(form)
#
# class EditProduct(UpdateView):
#     model = Product
#     fields = ['name', 'image', 'price', 'weight', 'calories', 'composition']
#     template_name = 'cart/edit_product.html'
#     context_object_name = 'product'
#
#
# class DeleteProduct(DeleteView):
#     model = Product
#     template_name = 'cart/detail.html'
#     context_object_name = 'product'
#     success_url = reverse_lazy('/')
