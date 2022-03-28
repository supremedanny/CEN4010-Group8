from django.contrib import admin
from .models import Cart

class adminShoppingCart(admin.ModelAdmin):
    list_display = ('books')


admin.site.register(Cart,adminShoppingCart)
