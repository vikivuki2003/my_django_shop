import os

from django.contrib import messages
import requests
from django.shortcuts import render, get_object_or_404, redirect

from app.settings import BASE_DIR
from orders.models import Order
from payment.forms import CheckoutForm
from payment.models import PaymentMethod
from msilib.schema import Environment

from environ import Env
env = Env()
env_path = os.path.join(BASE_DIR, '.env')
env.read_env(env_path)
STRIPE_SECRET = env('STRIPE_SECRET_KEY')


def shipping(request):
    ...

def checkout(request):

    orders = Order.objects.filter(user=request.user, status='In processing')

    if orders.exists():
        order = orders.first()
    else:
        messages.error(request, 'У вас нет активных заказов.')
        return redirect('some-view')

    payment_methods = PaymentMethod.objects.all()

    return render(request, 'payment/checkout.html', {
        'order': order,
        'payment_methods': payment_methods,
    })

def complete_order(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            orders = Order.objects.filter(user=request.user, status='In processing')

            if not orders.exists():
                return handle_error(request, 'У вас нет активных заказов.')

            order = orders.first()
            payment_method = request.POST.get('stripe-payment') or request.POST.get('yookassa-payment')

            if not payment_method:
                return handle_error(request, 'Выберите метод оплаты.')

            # Обработка платежа
            if payment_method == 'stripe-payment':
                return process_stripe_payment(order, request)

            elif payment_method == 'yookassa-payment':
                return process_yookassa_payment(order, request)

        return handle_error(request, 'Пожалуйста, исправьте ошибки в форме.')

    form = CheckoutForm()
    return render(request, 'payment/checkout.html', {'form': form})

def handle_error(request, message):
    messages.error(request, message)
    print(message)
    return redirect('payment:checkout')

def process_stripe_payment(order, request):
    try:
        # Получаем токен из запроса
        token = request.POST.get('stripe_token')
        if not token:
            return handle_error(request, "Токен Stripe не был предоставлен.")

        # Устанавливаем заголовки для запроса
        headers = {
            'Authorization': f'Bearer {STRIPE_SECRET}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Выполняем запрос на оплату
        response = requests.post('https://api.stripe.com/v1/charges', data={
            'amount': order.payment_on_get,
            'currency': 'usd',
            'source': token,
            'description': 'Order Payment'
        }, headers=headers)  # Не забывайте добавить заголовки

        # Обработка ответа от Stripe
        if response.status_code == 200:
            return redirect('payment:payment_success')
        else:
            error_message = response.json().get('error', {}).get('message', 'Неизвестная ошибка')
            return handle_error(request, f"Ошибка от Stripe: {error_message}")

    except Exception as e:
        return handle_error(request, f"Ошибка обработки платежа: {str(e)}")

def process_yookassa_payment(order, request):
    payload = {
        "amount": {
            "value": str(order.total_amount),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://example.com/payment/success/"
        },
        "capture": True,
        "description": "Order Payment"
    }
    headers = {
        "Authorization": "Bearer YOUR_YOOKASSA_API_KEY"
    }

    try:
        response = requests.post('https://api.yookassa.ru/v3/payments', json=payload, headers=headers)

        if response.status_code == 201:
            confirmation_url = response.json().get('confirmation').get('confirmation_url')
            return redirect(confirmation_url)

    except Exception as e:
        return handle_error(request, f"Ошибка обработки платежа: {str(e)}")

def payment_success(request):
    ...

def payment_failure(request):
    ...