from users.models import Account
from .models import Cart
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['idd']


class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()
    class Meta:
        model = Cart
        fields = ['created_by', 'order_items']

