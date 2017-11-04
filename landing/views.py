from django.shortcuts import render

from products.models import *


def CakeShopLanding(request):
    products = ProductImage.objects.filter(is_active=True)
    return render(request, 'CakeShopLanding/index.html', locals())
