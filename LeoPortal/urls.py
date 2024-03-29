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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as auth_views

import leo.views as views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='account/login.html'), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='account_logout'),
    path('signup/', auth_views.SignupView.as_view(template_name='account/register.html'), name='account_signup'),
    path('account/password/reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='account_reset_password'),
    path('account/password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='account_reset_password_done'),
    re_path('^account/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', auth_views.PasswordResetFromKeyView.as_view(template_name='account/password_reset_from_key.html'), name='account_reset_password_from_key'),
    path('account/password/reset/key/done/', auth_views.PasswordResetFromKeyDoneView.as_view(template_name='account/password_reset_from_key_done.html'), name='account_reset_password_from_key_done'),
    path("account/password/change/", auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name="account_change_password"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", auth_views.ConfirmEmailView.as_view(template_name='account/email_confirm.html'),name="account_confirm_email"),
    path('account/verification_sent/', auth_views.EmailVerificationSentView.as_view(template_name='account/verification_sent.html'),name="account_email_verification_sent"),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('admin/', admin.site.urls),
    path('newsletter/', views.newsletterView.as_view(), name = 'newsletter'),
    path('calendar/', views.calenderView.as_view(), name = 'calendar'),
    path('account/', views.account, name = 'account'),
    path('exclusive_content/', views.exclusiveView.as_view(), name = 'exclusive'),
    path('exclusive/<int:pk>', views.exclusiveDetailView.as_view(), name = 'exclusiveDetail'),
    path('membership/', views.cardView.as_view(), name = 'membership'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

