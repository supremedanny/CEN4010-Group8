from urllib import request
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from users.models import Account
from .models import Cart
from .serializers import UserSerializer, CartSerializer
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('idd')
    serializer_class = UserSerializer


class CartViewSet(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    '''
    def cartItems(request):
        if request.method == ('GET'):
            queryset = Cart.objects.all()
            serializer_class = CartSerializer

            return queryset
            '''
'''
    def addItem(request):
        if request.method == ('POST'):
            queryset = Cart.objects.all().order_by('id')
            serializer_class = CartSerializer

            return queryset

    def deleteItem(request):
        if request.method == ('DELETE'):
            queryset = Cart.objects.all().order_by('id')
            serializer_class = CartSerializer

            return queryset
'''