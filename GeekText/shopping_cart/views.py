from urllib import request
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Cart
from .serializers import UserSerializer, CartSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer


