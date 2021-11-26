from django.shortcuts import render
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
    context = {
        'links_menu': ProductCategory.objects.all(),
        'title': 'продукты'
    }
    return render(request, "mainapp/products.html", context)



