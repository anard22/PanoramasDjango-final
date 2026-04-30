from django.urls import path
from .views import panoramas_api, categorias_api

urlpatterns = [
    path('panoramas/', panoramas_api, name='panoramas_api'),
    path('categorias/', categorias_api, name='categorias_api'),
]