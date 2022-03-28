from django.db import models
from isbn_field import ISBNField

# Create your models here.

# Had to make one of the parts from Feature 4 to begin Feature 1.
# Allows you to create a book and apply the ISBN, genre, and rating.


class Genre(models.Model):
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    genre = models.ManyToManyField(Genre, related_name='books')
    rating = models.FloatField(null=True, blank=True)
    sales = models.IntegerField(null=True, blank=True)
    isbn = ISBNField()
    on_delete=models.DO_NOTHING,
    related_name="books"

# This serves to give the labels on the database human-readable names.

    def __str__(self):
        return self.title