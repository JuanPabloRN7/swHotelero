from django.urls import path

from . import views

urlpatterns = [
    path('nuevo/', views.registrar, name='crear_servicio'),   
]