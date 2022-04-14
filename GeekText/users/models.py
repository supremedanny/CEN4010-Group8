from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save


class AccountManage(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have email for account')
       
        email = self.normalize_email(email),#lowercase
        user = self.model(
            
            email = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = None #models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=60,blank=True)
    address = models.CharField(max_length=60,blank=True)
    idd = models.IntegerField(primary_key=True)


    objects = AccountManage()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    

    def __str__(self):
        return self.email

#does user have admin to do admin things
    def has_perm(self, perm, obj=None):
        return self.is_admin
#user have module permissions?
    def has_module_perms(self, app_label):
        return True
#credit card model for database
#method name to grab the name of user using the foreignkey referencing the tuple
#in the user table to show name of user for a GET request
class CreditCard(models.Model):
    cardnumber = models.CharField(max_length=16, unique=True)
    owner = models.ForeignKey(Account,on_delete=models.CASCADE)
    
    def name(self):
        return self.owner.name
