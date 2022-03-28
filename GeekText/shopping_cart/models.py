from django.db import models
from books.models import Book
from users.models import Account



class Cart(models.Model):
    """Let Cart be a meta. And order_items is reverse relation"""
    created_by = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    # Use ORM here to help you get the count() of each item
    # 1 item represent 1 qty
    order_items = models.ManyToManyField(Book)



'''
class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
   

    def __str__(self):
        return "{} - {}".format(self.user,
                                self.item,)
'''
