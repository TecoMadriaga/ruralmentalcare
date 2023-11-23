from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    #path('', views.lista_profesionales, name='lista_profesionales'),
    path('', views.index, name='index'),
    path('nueva_cita/', views.nueva_cita, name='nueva_cita'),
    path('profesionales/', views.lista_profesionales, name='lista_profesionales'),
    path('profesionales/<int:pk>/', views.detalle_profesional, name='detalle_profesional'),
    path('profesionales/<int:profesional_id>/nueva_cita/', views.nueva_cita, name='nueva_cita'),
    path('recursos/', views.lista_recursos, name='lista_recursos'),
    path('registro_profesional', views.registro_profesional, name='registro_profesional'),
    path('registro/', views.registro, name='registro'),
]
