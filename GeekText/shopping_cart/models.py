from django.db import models
from books.models import Book
from users.models import Account
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.conf import settings

from functools import partial



'''
class Cart(models.Model):
    """Let Cart be a meta. And order_items is reverse relation"""
    created_by = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    # Use ORM here to help you get the count() of each item
    # 1 item represent 1 qty
    order_items = models.ManyToManyField(Book)

class CartItem(models.Model):
    """A model that contains data for an item in the shopping cart."""
    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Book,
        related_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.product.title, self.quantity)
'''

#The one below is the latest working one

class Cart(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    

