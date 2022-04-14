from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Book

# Register our book model in the admin panel.

#admin.site.register(Book)

class TopSellersFilter(admin.SimpleListFilter):
    title = ('sales')
    parameter_name = 'sales'

    def lookups(self, request, model_admin):
        return (
            ('1', ('Top Sellers')),
            ('2', ('Bottom Sellers')),
        )

    def queryset(self, request, queryset):
        if self.value() =='1':
            return queryset.order_by('-sales')

        if self.value() =='2':
            return queryset.order_by('sales')

class RatingsFilter(admin.SimpleListFilter):
    title = ('rating')
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return (
            ('0', ('0.5 & Higher')),
            ('1', ('1 & Higher')),
            ('2', ('1.5 & Higher')),
            ('3', ('2 & Higher')),
            ('4', ('2.5 & Higher')),
            ('5', ('3 & Higher')),
            ('6', ('3.5 & Higher')),
            ('7', ('4 & Higher')),
            ('8', ('4.5 & Higher')),
        )

    def queryset(self, request, queryset):
        if self.value() =='0':
            return queryset.filter(rating__gte=0.5)

        if self.value() =='8':
            return queryset.filter(rating__gte=4.5)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'rating', 'sales')
    list_filter = ('genre', TopSellersFilter, RatingsFilter)
    search_fields = ('title',)

admin.site.register(Book, BookAdmin)




