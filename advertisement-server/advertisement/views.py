from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Product, Customer, Order
from .forms import CustomerForm, OrderForm

# Create your views here.
@csrf_exempt
def home(request):

    return render(request, 'index.html')

def product(request, sku, slug):
    context = {
        'sku': sku,
    }
    return render(request, 'index.html', context)

def giohang(request, sp_id):
    success = False
    try:
        product = Product.objects.get(pk=sp_id)
    except Product.DoesNotExist:
        return redirect('home')

    context = {
        'success': success,
        'product': product,
        'sp_id': sp_id
    }

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)

        if customer_form.is_valid() and order_form.is_valid():
            customer_data = Customer(**customer_form.cleaned_data)
            customer = Customer.objects.filter(
                mobile_phone=customer_data.mobile_phone
            )

            if not customer.exists():
                customer = customer_data.save()
                customer = customer_data
            else:
                customer = customer.first()

            order = Order(**order_form.cleaned_data)
            order.product = product
            order.customer = customer
            order.status = Order.STATUS_TYPE.cx
            order.save()
            return redirect('hoantat', or_id = order.id)

    return render(request, 'gio-hang.html', context)

def hoantat(request, or_id):
    try:
        order = Order.objects.get(pk=or_id)
    except Order.DoesNotExist:
        return redirect('home')
    
    context = {
        'success': 'success',
        'order': order
    }

    return render(request, 'hoan-tat.html', context)


def vanchuyen(request):

    return render(request, 'chinh-sach-van-chuyen.html')


def doitra(request):

    return render(request, 'chinh-sach-doi-tra.html')

def dieukhoanthanhtoan(request):

    return render(request, 'dieu-khoan-dieu-kien-thanh-toan.html')
