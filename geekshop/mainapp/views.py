import random

from django.shortcuts import render, get_object_or_404
import json
from mainapp.models import Product, ProductCategory

# Create your views here.
from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return sum(list(Basket.objects.filter(user=user).values_list('quantity', flat=True)))
    return 0


def index(request):
    context = {'title': 'магазин',
               'products': Product.objects.all()[:4],
               'basket': get_basket(request.user)
               }
    return render(request, "mainapp/index.html", context)


def contact(request):
    context = {
        'title': 'контакты',
        'basket': get_basket(request.user)
               }
    return render(request, "mainapp/contact.html", context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {
                'name': 'все',
                'pk': 0
            }
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)
        context = {
            'links_menu': links_menu,
            'title': 'продукты',
            'category_item': category_item,
            'products': products_list,
            'basket': get_basket(request.user)
        }
        return render(request, "mainapp/products_list.html", context)

    hot_product = random.sample(list(Product.objects.all()), 1)[0]
    same_products = Product.objects.all()[3:5]
    context = {
        'links_menu': ProductCategory.objects.all(),
        'title': 'продукты',
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request.user)
    }

    return render(request, "mainapp/products.html", context)
