from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('footer/', views.footer, name = 'footer'),
    path('header/', views.header, name = 'Header'),
]