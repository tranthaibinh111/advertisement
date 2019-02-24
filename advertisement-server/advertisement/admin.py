from django.contrib import admin

from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info customer ', {
            'fields': ('full_name', 'mobile_phone', 'address', 'note')
        }),
        ('Info order status', {
            'fields': ('status',)
        }),
    )

    list_display = ('full_name', 'mobile_phone', 'status', 'order_date',)
    ordering = ('-order_date',)
    search_fields = ('full_name',)
