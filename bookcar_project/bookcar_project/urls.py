"""
URL configuration for bookcar_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from customer_app import views as customer_views
from driver_app import views as driver_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cabs/', driver_views.cab_list),
    path('cabs/<id>/', driver_views.cab_detail),
    path('customers/', customer_views.customer_list),
    path('customers/<id>/', customer_views.customer_detail),
    path('drivers/', driver_views.driver_list),
    path('drivers/<id>/', driver_views.driver_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
