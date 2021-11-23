from django.shortcuts import render
import json

# Create your views here.


def index(request):
    context = {'title': 'магазин'}
    return render(request, "mainapp/index.html", context)


def contact(request):
    context = {'title': 'контакты'}
    return render(request, "mainapp/contact.html", context)


# links_menu = [
#     {
#         'url': 'products',
#         'title': 'Все'
#     },
#     {
#         'url': 'products_home',
#         'title': 'Дом'
#     },
#     {
#         'url': 'products_office',
#         'title': 'Офис'
#     },
#     {
#         'url': 'products_modern',
#         'title': 'Модерн'
#     },
#     {
#         'url': 'products_classic',
#         'title': 'Классика'
#     },
# ]


with open('static/json/products_menu.json', 'r', encoding='utf-8') as read_file:
    links_menu = json.load(read_file)


def products(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты'
    }
    return render(request, "mainapp/products.html", context)


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты для дома'
    }
    return render(request, "mainapp/products.html", context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты для офиса'
    }
    return render(request, "mainapp/products.html", context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты модерн'
    }
    return render(request, "mainapp/products.html", context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты классика'
    }
    return render(request, "mainapp/products.html", context)
