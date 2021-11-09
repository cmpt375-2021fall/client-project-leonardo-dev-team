from django.urls import path

from leo import views

#Raven's experimental nav drop down bar:
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showlist/', views.showlist, name='showlist'),
]
