from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Products
from users.models import User


class PaymentMethod(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)  # Assuming you have an Order model in your orders app
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust precision as needed
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment {self.id} by {self.user.username} - {self.amount}'


class Refund(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Refund for Payment {self.payment.id} - Amount: {self.amount}'

class TransactionLog(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # e.g., 'created', 'updated', 'refunded'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction Log for Payment {self.payment.id} - Action: {self.action}'