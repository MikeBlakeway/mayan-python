
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="mayan/index.html")),
    path('about/', TemplateView.as_view(template_name="mayan/about.html")),
    path('services/', TemplateView.as_view(template_name="mayan/services.html")),
    path('packages/', TemplateView.as_view(template_name="mayan/packages.html")),
    path('contact/', TemplateView.as_view(template_name="mayan/contact.html")),
]
