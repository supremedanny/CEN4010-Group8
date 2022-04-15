from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'rating', 'sales', 'isbn')