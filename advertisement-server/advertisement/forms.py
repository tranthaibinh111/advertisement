from django import forms

from .models import Product, Customer, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'mobile_phone', 'address')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('amount', 'total_price', 'note',)
