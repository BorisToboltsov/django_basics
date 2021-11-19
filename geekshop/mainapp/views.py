from django.shortcuts import render

# Create your views here.


def index(request):
    tit = {'title': 'Магазин'}
    return render(request, "mainapp/index.html", tit)


def products(request):
    tit = {'title': 'Продукты'}
    return render(request, "mainapp/products.html", tit)


def contact(request):
    tit = {'title': 'Контакты'}
    return render(request, "mainapp/contact.html", tit)


def menu(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
    return render(request, 'inc_categories_menu.html', links_menu)
