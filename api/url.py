from django.urls import path
from . import views
urlpatterns = [
    path("createorder", views.home),
    path("returnurl", views.returnurl),
    path("clienturl", views.clienturl)
    
]