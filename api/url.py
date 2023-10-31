from django.urls import path
from . import views
urlpatterns = [
    path("createorder", views.order),
    path("returnurl", views.returnurl),
    path("clienturl", views.clienturl),
    path("products", views.product_list),
    path("clear", views.clear_cache),
    path("", views.home)

    
]