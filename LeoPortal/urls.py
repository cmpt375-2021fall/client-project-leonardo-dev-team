"""LeoPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from leo import views
from django.contrib.auth import views as auth_views

import leo.views as views

urlpatterns = [
    #login
    path('', views.register_request),
    path('register/', views.register_request, name='register'),

    # path('', views.homepage, name="homepage"),
    #
    path('login/', views.login_request, name ='login_request'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('admin/', admin.site.urls),
    path('newsletter/', views.newsletter, name = 'newsletter'),
    path('calendar/', views.calendar, name = 'calendar'),

]
