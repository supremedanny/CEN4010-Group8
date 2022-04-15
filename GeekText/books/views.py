from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

class GenreFilter(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^genre']

class SalesFilter(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-sales']

class RatingsFilter(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'rating': ['gte', 'lte']
    }

class IDFilter(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['id']