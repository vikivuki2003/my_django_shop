from app.urls import urlpatterns
from . import views
from django.urls import path

app_name = 'payment'

urlpatterns = [
    path('shipping/', views.shipping, name='shipping'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-failure/', views.payment_failure, name='payment-failure'),

]