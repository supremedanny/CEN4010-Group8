from django.urls import path

"""geeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shopping_cart.views import (CartViewSet, create_Cart, cart_update, deleteFromCart)
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', include("webapi.urls")),
    #path('home/', home_view),
    path('api/users/', include('users.urls')),
    path('viewratings/', include('rating.urls')),
    path('', include('books.urls')),
    #urls for cart
    path('api/shopping_cart/', include('shopping_cart.urls')),
    path('cart_upate/',cart_update, name="cart_update"),
    path('create_cart/',create_Cart, name="create_cart"),
    path('deleteFromCart/<int:item_id>/',deleteFromCart, name="deleteFromCart"),

]
