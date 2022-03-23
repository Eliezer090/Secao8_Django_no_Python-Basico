from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.metodo, name='metodo'),
]
