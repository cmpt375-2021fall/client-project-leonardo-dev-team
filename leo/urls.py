from django.urls import path

from leo import views

urlpatterns = [
    path('', views.home, name = 'home'),

]

