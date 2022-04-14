from django.contrib import admin
from .models import Rating

# Register your models here.

# Register our book model in the admin panel.

class RatingAdmin(admin.ModelAdmin):
    list_display = ('Add Rating', 'Add Comment')

    def ratings(self, obj):
        return obj.ratings

admin.site.register(Rating)
