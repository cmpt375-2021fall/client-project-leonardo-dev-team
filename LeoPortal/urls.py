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
from django.urls import path, include

import leo.views as views
from leo.views import exclusiveDetailView
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', auth_views.SignupView.as_view(template_name='registration/register.html'), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('admin/', admin.site.urls),
    path('newsletter/', views.newsletter, name = 'newsletter'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('account/', views.account, name = 'account'),
    path('exclusive_content/', views.exclusive, name = 'exclusive'),
    path('exclusive/<int:pk>', exclusiveDetailView.as_view(), name = 'exclusiveDetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
