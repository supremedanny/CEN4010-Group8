from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.serializers import PasswordChangeSerializer, RegistrationSerializer, AccountInfoSerializer, AccountInfoChangeSerializer,CreditCardSerializer,CardRegistrationSerializer
from users.models import Account, CreditCard
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.filters import SearchFilter

#to register a user
@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "New user created!"
            data['email'] = account.email
        #    data['username'] = account.username
            data['address'] = account.address
            data['name'] = account.name
        else:
            data = serializer.errors
        return Response(data)

#to register a card to a user
#unfortunately, I could not do it by the name of the user. 
@api_view(['POST', ])
def card_registration_view(request):
    if request.method == 'POST':
        serializer = CardRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            creditcard = serializer.save()
            data['response'] = "New Credit Card created!"
            data['cardnumber'] = creditcard.cardnumber
            return Response(data=data)
        else:
            data = serializer.errors
        return Response(data=data)

#list users api/users/list
class PropertiesView(generics.ListAPIView):
    serializer_class = AccountInfoSerializer
    def get_queryset(self):
        queryset = Account.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

#list cards user api/users/cardlist
class CardView(ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    filter_backends = (SearchFilter, )
    search_fields = ['owner__username']

#change users account information
@api_view(['PUT', ])
def account_update_view(request, email):
    account = Account.objects.get(email=email)
    if request.method == 'PUT':
        serializer = AccountInfoChangeSerializer(account, data = request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Updated'
            data['email'] = account.email
            data['address'] = account.address
            data['name'] = account.name
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to show user's account information
@api_view(['GET', ])
def account_info_view(request,email):
    account = Account.objects.get(email=email)
    if request.method == 'GET':
        serializer = AccountInfoSerializer(account)
        return Response(serializer.data)

#to show user's credit cards linked to them
@api_view(['GET', ])
def credit_card_view(request,email):
    owner = CreditCard.objects.get(email=email)
    if request.method == 'GET':
        serializer = CreditCardSerializer(owner,data = request.data)
        return Response(serializer.data)

#to change user's password
@api_view(['PUT', ])
def password_change_view(request,email):
    account = Account.objects.get(email=email)
    if request.method == 'PUT':
        serializer = PasswordChangeSerializer(account,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Password Changed'
            account.set_password(serializer.data.get("new_password"))
            account.save()
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


