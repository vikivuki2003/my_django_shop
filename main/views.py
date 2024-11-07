from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories, Products


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Naomi - Main'
        context['content'] = "Shop Naomi"
        context['products'] = Products.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Naomi - About us'
        context['content'] = "About us"
        return context

class DeliveryPaymentView(TemplateView):
    template_name = 'main/delivery_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Naomi - Delivery and Payment'
        context['content'] = "Delivery and Payment options"
        return context

class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Naomi - Contacts'
        context['content'] = "Contact information"
        return context
    

# def index(request):

#     context = {
#         'title': 'Home - Главная',
#         'content': "Магазин мебели HOME",
#     }

#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Home - О нас',
#         'content': "О нас",
#         'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
#     }

#     return render(request, 'main/about.html', context)