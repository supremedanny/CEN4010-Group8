from rest_framework import serializers
from users.models import Account, CreditCard

#Uses user email
class RegistrationSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Account
        fields = ['email','password','address','name']
       
    def save(self):
        account = Account(
            email = self.validated_data['email'],
           # username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        account.address = self.validated_data['address']
        account.name = self.validated_data['name']
        account.set_password(password)
        account.save()
        return account

#This is for the GET part of the API    
class AccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['idd','name','email', 'address']

#This is for the PUT part of the API so user can change name and address
class AccountInfoChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name','address']
        
    address = serializers.CharField
    name = serializers.CharField
       

#This is for the PUT part of the API so user can change password
class PasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['old_password','new_password']
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

#This is for the POST part of the API so user can register/create 
#their credit card
class CardRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['cardnumber','owner']

    def save(self):
        creditcard = CreditCard(
            cardnumber = self.validated_data['cardnumber'],
            owner = self.validated_data['owner']    
        )
        creditcard.save()
        return creditcard

#to POST/GET in JSON
# ID shows the primary key, card number shows the credit card number
# and name shows the user's name that they used when creating an account       
class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id', 'cardnumber', 'name']

