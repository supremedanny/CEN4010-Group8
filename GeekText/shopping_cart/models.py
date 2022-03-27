from django.db import models
from books.models import Book


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name,
                                     self.created_at,
                                     self.updated_at)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.user,
                                               self.item,
                                               self.quantity,
                                               self.created_at,
                                               self.updated_at)


