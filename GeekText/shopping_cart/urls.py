from django.urls import path,include
from shopping_cart.views import (CartViewSet, create_Cart, cart_update, deleteFromCart)



#URL CONFIG
#urlpatterns = [
    #path('cart',views.say_hello)
#]

app_name = 'shopping_cart'

urlpatterns = [
    path('', CartViewSet.as_view(), name = 'cart'),
    path('create_cart',create_Cart, name="create_cart"),
    path('cart_update',cart_update, name="cart_update"),
    path('deleteFromCart/<int:item_id>/',deleteFromCart, name="deleteFromCart"),
]
