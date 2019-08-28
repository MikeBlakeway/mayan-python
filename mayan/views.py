from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'mayan/index.html'


class AboutView(TemplateView):
    template_name = 'mayan/about.html'


class ServicesView(TemplateView):
    template_name = 'mayan/services.html'


class ProductsView(TemplateView):
    template_name = 'mayan/packages.html'


class ContactView(FormView):
    template_name = 'mayan/contact.html'
    form_class = ContactForm
    success_url = '/success/'

    # Form validation method
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'mayan/success.html'
