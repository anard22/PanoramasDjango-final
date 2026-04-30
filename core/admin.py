
from django.contrib import admin
from .models import Perfil, Panorama, Categoria


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'rut', 'telefono')
    search_fields = ('user__username', 'rut')


@admin.register(Panorama)
class PanoramaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'lugar', 'fecha', 'creador')
    search_fields = ('titulo', 'lugar')
    list_filter = ('fecha',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

