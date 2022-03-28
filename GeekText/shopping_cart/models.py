from django.db import models
from books.models import Book

class Cart(models.Model):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
   

    def __str__(self):
        return str(self)

