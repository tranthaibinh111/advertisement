from django.contrib import admin

from .models import Product, Customer, Order


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info product ', {
            'fields': ('name', 'image', 'price')
        }),
    )

    list_display = ('name', 'price', 'image', 'create_date',)
    ordering = ('-create_date',)


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info customer ', {
            'fields': ('full_name', 'mobile_phone', 'address')
        }),
    )

    list_display = ('full_name', 'mobile_phone', 'create_date',)
    ordering = ('-create_date',)
    search_fields = ('full_name',)


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info customer ', {
            'fields': ('customer', 'product', 'amount')
        }),
        ('Info order status', {
            'fields': ('status',)
        }),
        ('Info comment', {
            'fields': ('note',)
        }),
    )

    list_display = ('full_name', 'mobile_phone', 'product_name', 'amount', 'total_price', 'status', 'order_date',)
    ordering = ('-order_date',)
    search_fields = ('customer__full_name',)

    def full_name(self, obj):
        if obj and obj.customer:
            return obj.customer.full_name
        else:
            return None

    def mobile_phone(self, obj):
        if obj and obj.customer:
            return obj.customer.mobile_phone
        else:
            return None

    def product_name(self, obj):
        if obj and obj.product:
            return obj.product.name
        else:
            return None
