from django.db import models
from model_utils import Choices

# Create your models here.
class Order(models.Model):
    STATUS_TYPE = Choices(
        ('cx', u'Chờ xác định'),
        ('dx', u'Đã xác nhận'),
        ('dg', u'Đã gửi đi'),
        ('h', u'Hủy'),
    )

    full_name = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=2,choices=STATUS_TYPE, default='cx')
    order_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} SDT: {}".format(self.full_name, self.mobile_phone)
