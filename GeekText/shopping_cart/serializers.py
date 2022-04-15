from users.models import Account
from .models import Cart
from rest_framework import serializers

'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['idd']
'''

#This is for the GET API call
class CartSerializer(serializers.ModelSerializer):
   # created_by = serializers.CurrentUserDefault()
    class Meta:
        model = Cart
        fields = ['user', 'item']

class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['cart_items']
        
    def save(self):
        cart = Cart(
           cart_items = self.validated_data['cart_items'],
        )
        cart.save()
        return cart