from django.contrib import admin
from .models import PaymentMethod, Payment

admin.site.register(PaymentMethod)
admin.site.register(Payment)
