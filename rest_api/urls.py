from django.urls import path
from .views import panoramas_api

urlpatterns = [
    path('panoramas/', panoramas_api, name='panoramas_api'),
]