from django.shortcuts import render, get_object_or_404
import json
from mainapp.models import Product, ProductCategory

# Create your views here.


def index(request):
    context = {'title': 'магазин',
               'products': Product.objects.all()[:4]
               }
    return render(request, "mainapp/index.html", context)


def contact(request):
    context = {'title': 'контакты'}
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
            'links_menu': ProductCategory.objects.all(),
            'title': 'продукты',
            'category_item': category_item,
            'products': products_list
        }
        return render(request, "mainapp/products_list.html", context)

    context = {
        'links_menu': ProductCategory.objects.all(),
        'title': 'продукты'
    }

    return render(request, "mainapp/products.html", context)
