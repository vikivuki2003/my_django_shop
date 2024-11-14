from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from orders.models import Order
from payment.models import PaymentMethod


def shipping(request):
    ...

def checkout(request):
    order = get_object_or_404(Order, user=request.user, status='In processing')
    payment_methods = PaymentMethod.objects.all()
    # Если у вас есть поля для ввода адреса доставки в форме заказа
    if request.method == 'POST':
        # Обработка формы с данными о доставке
        delivery_address = request.POST.get('delivery_address')
        order.delivery_address = delivery_address
        order.save()
        messages.success(request, 'Адрес доставки обновлен!')

    return render(request, 'payment/checkout.html', {
        'order': order,
        'payment_methods': payment_methods,
        'delivery_address': order.delivery_address,  # Отображение текущего адреса доставки
    })

def complete_order(request):
    ...

def payment_success(request):
    ...

def payment_failure(request):
    ...