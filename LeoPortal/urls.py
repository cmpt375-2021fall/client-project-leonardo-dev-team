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
from leo.views import exclusiveView, exclusiveDetailView
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as auth_views
# from django.contrib.auth import views as auth_views

# auth_views.

urlpatterns = [
    #login
    # path('', views.login_request),
    # path('accounts/login/', auth_views.auth_login.,{'authentication_form': CustomAuthForm}, name='login'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('accounts/', include('allauth.urls')),
      path('accounts/', include('allauth.urls')),

                  # path('accounts/', include('django.contrib.auth.urls'),  kwargs={"authentication_form":CustomAuthForm}),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('register/', views.register_request, name='register'),
    # path('login/', views.login_request, name ='login_request'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('admin/', admin.site.urls),
    path('newsletter/', views.newsletter, name = 'newsletter'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('account/', views.account, name = 'account'),
    #path('exclusive_content/', views.exclusive, name = 'exclusive'),
    path('exclusive_content', exclusiveView.as_view(), name = 'exclusive'),
    path('exclusive/<int:pk>', exclusiveDetailView.as_view(), name = 'exclusiveDetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
