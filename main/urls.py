
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views import debug

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', debug.default_urlconf),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
