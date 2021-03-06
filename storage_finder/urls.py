"""storage_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

# Use static() to add url mapping to serve static files during development (only)

from finder import views
from django.urls import path
from django.conf import settings

from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    url(r'^package/(?P<id>.+?)/$', views.package, name='package'),

    path('', RedirectView.as_view(url='finder/')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
