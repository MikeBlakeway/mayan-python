
from django.urls import path
from django.views.generic import TemplateView
from mayan.views import ContactView


urlpatterns = [
    path('', TemplateView.as_view(template_name="mayan/index.html"), name="index"),
    path('about/', TemplateView.as_view(template_name="mayan/about.html"), name="about"),
    path('services/', TemplateView.as_view(template_name="mayan/services.html"), name="services"),
    path('packages/', TemplateView.as_view(template_name="mayan/packages.html"), name="packages"),
    path('contact/', ContactView.as_view(), name="contact"),
]
