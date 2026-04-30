from django.contrib import admin
from .models import Perfil, Panorama


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'rut', 'telefono')
    search_fields = ('user__username', 'rut')


@admin.register(Panorama)
class PanoramaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'lugar', 'fecha', 'creador')
    search_fields = ('titulo', 'lugar')
    list_filter = ('fecha',)
