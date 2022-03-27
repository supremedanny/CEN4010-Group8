import email
from rest_framework import serializers
from users.models import Account, CreditCard

#Still need to make email the username
class RegistrationSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Account
        fields = ['email','username','password','address','name']
       
    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
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
        fields = ['idd','username','address','name','email']

#This is for the PUT part of the API
#I believe needs work still. 
class AccountInfoChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username','address','name']
        
    def save(self):
        account = Account(
           username = self.validated_data['username'],
        )
        account.address = self.validated_data['address']
        account.name = self.validated_data['name']
        account.save()
        return account

#This is for the PUT part of the API so user can change password
class PasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['old_password','new_password']
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

#still working on this
"""
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
        return creditcard"""
#still working on this        
"""
class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id', 'cardnumber', 'owner']"""