from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('footer/', views.footer),
    path('header/', views.header),
]