from __future__ import unicode_literals
from __future__ import print_function
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from books.models import Book
from users.models import Account
from .models import Cart
from .serializers import CartSerializer, CartUpdateSerializer
from rest_framework import generics



class CartViewSet(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
@csrf_exempt

@api_view(['POST', ])
def create_Cart(request):
    
    if request.method == 'POST':
        data= JSONParser().parse(request)
        serializer = CartSerializer(data=data)
        
        if serializer.is_valid():
            createdcart = serializer.save()
            data['response'] = "Cart created within database"
            data['user'] = createdcart.user
            data['item'] = createdcart.item
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)


@api_view(['PUT', ])
def cart_update(request, email):
    account = Account.objects.get(email=email)
    if request.method == 'PUT':
        serializer = CartUpdateSerializer(account, data = request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Updated'
            data['cart_items'] = account.cart_items
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteFromCart(request, item_id):
    if request.method == 'DELETE':
        Cart.objects.filter(item_id = item_id).delete()
        return HttpResponse(status = 204)






"""Add an item to a user's cart.
        Adding to cart is disallowed if there is not enough inventory for the
        product available. If there is, the quantity is increased on an existing
        cart item or a new cart item is created with that quantity and added
        to the cart.
        Parameters
        ----------
        request: request
        Return the updated cart.
        """



        
'''
#NEEDS TO BE DONE
    @api_view(['DELETE'])
    def remove_from_cart(self, request, pk=None):
        """Remove an item from a user's cart.
        Like on the Everlane website, customers can only remove items from the
        cart 1 at a time, so the quantity of the product to remove from the cart
        will always be 1. If the quantity of the product to remove from the cart
        is 1, delete the cart item. If the quantity is more than 1, decrease
        the quantity of the cart item, but leave it in the cart.
        Parameters
        ----------
        request: request
        Return the updated cart.
        """
        cart = self.get_object()
        try:
            product = Book.objects.get(
                pk=request.data['product_id']
            )
        except Exception as e:
            print (e)
            return Response({'status': 'fail'})

        try:
            cart_item = CartItem.objects.get(cart=cart,product=product)
        except Exception as e:
            print (e)
            return Response({'status': 'fail'})

        # if removing an item where the quantity is 1, remove the cart item
        # completely otherwise decrease the quantity of the cart item
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()

        # return the updated cart to indicate success
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @api_view(['GET', ])
    def cartItems(request):
        if request.method == ('GET'):
            queryset = Cart.objects.all()
            serializer_class = CartSerializer
            return queryset



'''
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

'''
@login_required
@require_POST
def shopping_cart_submit(request):
    books = list(request.user.shopping_cart.all())
    request.user.books.add(*books)
    request.user.shopping_cart.clear()
    request.user.save()

    for book in books:
        book.holders_count += 1
        book.save()

    return redirect("shopping_cart")

@login_required
@require_POST
def shopping_cart_add(request):
    form = CartForm(request.POST)
    if not form.is_valid():
        return redirect("/")
    book_pk = form.cleaned_data.get("book_pk")
    try:
        book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExists:
        return redirect("/")

    request.user.shopping_cart.add(book)
    request.user.save()
    return redirect(form.cleaned_data.get("next_link"))

@login_required
@require_POST
def shopping_cart_remove(request):
    form = CartForm(request.POST)
    if not form.is_valid():
        return redirect("/")
    book_pk = form.cleaned_data.get("book_pk")
    try:
        book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExists:
        return redirect("/")

    request.user.shopping_cart.remove(book)
    request.user.save()
    return redirect(form.cleaned_data.get("next_link"))
    '''