"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from res.views import home_view, reserve_form,prev_view, today_view, next_view, check_table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('reserve/<int:id>/', reserve_form, name='reserve'),
    path('prev/', prev_view, name='prev'),
    path('today/', today_view, name='today'),
    path('next/', next_view, name='next'),
    path('check/', check_table, name='check')
]
