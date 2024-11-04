from django.urls import path
# from django.views.decorators.cache import cache_page

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('delivery_payment/', views.DeliveryPaymentView.as_view(), name='delivery_payment'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('about/', cache_page(60)(views.AboutView.as_view()), name='about'),
# ]