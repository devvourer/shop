from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None, sub_category_slug=None):
    category = None
    sub_categories = None
    sub_category = None
    check = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        sub_categories = SubCategory.objects.filter(category=category)
        products = products.filter(category=category)
    if sub_category_slug:
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        products = Product.objects.filter(sub_category=sub_category)
        check = 1

    return render(request, 'shop_counter/product/list.html', locals())


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop_counter/product/detail.html', locals())
