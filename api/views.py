from django.shortcuts import render,redirect
from django.core.cache import cache#默認使用"default"名稱的redis
# from django_redis import get_redis_connection#使用自訂義redis名稱
from .models import Product
from django.http import HttpResponse,JsonResponse

def home(request):
    return render(request,'home.html')

def order(request):
    return render(request,'order.html')

def returnurl(request):
    print(request)

def clienturl(request):
    return render(request,'clientback.html')

def product_list(request):
    product_list = cache.get('product_list')
    if not product_list:
        product_list = list(Product.objects.values('name', 'description', 'quantity'))
        cache.set('product_list', product_list)
        print("我在這裡")
        print(cache.keys('*'))
    return render(request,'product.html',{'products': product_list})

def clear_cache(request):
    cache.clear()
    print("資料清除完成")
    return redirect('/api/createorder')
