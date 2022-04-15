
from django.contrib import admin
from django.urls import path, include
from shopping_cart.views import (CartViewSet, create_Cart, cart_update, deleteFromCart)




urlpatterns = [
      path('admin/', admin.site.urls),
    path('api/shopping_cart/', include('shopping_cart.urls')),
    path('api/users/', include('users.urls', 'users_api')),
    #api urls for shopping cart
    path('create_cart/',create_Cart, name="create_cart"),
    path('cart_upate/',cart_update, name="cart_update"),
    path('deleteFromCart/<int:item_id>/',deleteFromCart, name="deleteFromCart"),
]
