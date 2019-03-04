from django.db import models
from model_utils import Choices


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(default=0, max_digits=15, decimal_places=0)
    image = models.ImageField(null=True, blank=True, upload_to='static/images')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} SDT: {}".format(self.full_name, self.mobile_phone)


class Order(models.Model):
    STATUS_TYPE = Choices(
        ('cx', u'Chờ xác nhận'),
        ('dx', u'Đã xác nhận'),
        ('dg', u'Đã gửi đi'),
        ('h', u'Hủy'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    status = models.CharField(max_length=2, choices=STATUS_TYPE, default='cx')
    order_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.customer:
            return "{} SDT: {}".format(self.customer.full_name, self.customer.mobile_phone)
        return None
