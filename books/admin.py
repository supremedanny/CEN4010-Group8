from django.contrib import admin
admin.autodiscover()

# Register your models here.

# Import book model from the directory.
from .models import Book

# Register our book model in the admin panel.
admin.site.register(Book)