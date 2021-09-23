from django.shortcuts import render

import os
import json
#
MODULE_DIR = os.path.dirname(__file__)

from products.models import ProductsCategory, Product
# Create your views here.
#Контролер - функция
def index (request):
    context = {'tittle': 'GeekShop'}
    return render(request, 'index.html',context)

def products(request):
    db_categories = ProductsCategory.objects.all()
    db_products = Product.objects.all()
    context = {'tittle':'Каталог',
                        'products': db_products,
                        'categories': db_categories,
    }
    path_file = os.path.join(MODULE_DIR,'fixtures\goods.json')
    context['products'] = json.load(open(path_file,encoding='utf-8'))

    return render(request, 'products.html',context)


def test(request):
    context = {
        'title': 'geekshop',
        'user': 'Ivanov',
        'description': 'Добро пожаловать в geekshop',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 '},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 '},
        ],
        'promotion':True,
        'products_of_promotion': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 '},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'}
        ]
        }

    return render(request, 'test.html',context)