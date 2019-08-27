from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'mayan/index.html'


class AboutView(TemplateView):
    template_name = 'mayan/about.html'


class ServicesView(TemplateView):
    template_name = 'mayan/services.html'


class ProductsView(TemplateView):
    template_name = 'mayan/packages.html'


class ContactView(TemplateView):
    template_name = 'mayan/contact.html'
