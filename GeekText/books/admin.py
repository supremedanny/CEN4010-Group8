from django.contrib import admin
from books.models import Genre, Book

# Register your models here.

# Register our book model in the admin panel.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'sales', 'rating')

    def sales(self, obj):
        return obj.sales

admin.site.register(Genre)
admin.site.register(Book)
