from django.urls import path,include
from rest_framework import routers
from shopping_cart.views import CartViewSet,UserViewSet
from shopping_cart import views

router = routers.DefaultRouter()
router.register(r'cart', views.CartViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'cart-view/', CartViewSet, basename='CartViewSet')
router.register(r'user-view/', UserViewSet, basename='UserViewSet')


#URL CONFIG
#urlpatterns = [
    #path('cart',views.say_hello)
#]

urlpatterns = [
    path('', include((router.urls, 'GeekText.shopping_cart'))),
]