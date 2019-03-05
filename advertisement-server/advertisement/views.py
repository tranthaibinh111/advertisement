from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Product, Customer, Order
from .forms import CustomerForm, OrderForm

# Create your views here.
@csrf_exempt
def home(request):
    success = False
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = Order(**order_form.cleaned_data)
            order.status = Order.STATUS_TYPE.cx

            order_old = Order.objects.filter(mobile_phone=order.mobile_phone)
            if not order_old.exists():
                order.save()
                success = True
    context = {
        'success': success,
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
            if not customer.exist():
                customer = customer_data.save()
            else:
                customer = customer.first()

            order = Order(**order_form.cleaned_data)
            order.product = product
            order.customer = customer
            order.status = Order.STATUS_TYPE.cx
            order.save()

        context.update({'success': True})

        return redirect('giohang', sp_id)

    return render(request, 'gio-hang.html', context)


def thanhtoan(request):
    context = {
        'success': 'success',
    }

    return render(request, 'thanh-toan.html', context)


def hoantat(request):
    context = {
        'success': 'success',
    }

    return render(request, 'hoan-tat.html', context)


def vanchuyen(request):
    context = {
        'success': 'success',
    }

    return render(request, 'chinh-sach-van-chuyen.html', context)


def doitra(request):
    context = {
        'success': 'success',
    }

    return render(request, 'chinh-sach-doi-tra.html', context)
