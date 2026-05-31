from django.contrib import admin
from .models import Property

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'property_type',
        'price',
        'city',
        'is_available'
    )

    list_filter = (
        'property_type',
        'city',
        'is_available'
    )

    search_fields = (
        'title',
        'location',
        'city'
    )