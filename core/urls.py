from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Públicas
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),

    # Recuperación de contraseña (Django Auth)
    path(
        'recuperar/',
        auth_views.PasswordResetView.as_view(
            template_name='core/recuperar.html'
        ),
        name='recuperar'
    ),

    # Usuario
    path('perfil/', views.perfil, name='perfil'),

    # Administración (protegidas por rol)
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),

    # CRUD Panoramas
    path('panoramas/', views.listar_panoramas, name='listar_panoramas'),
    path('panoramas/crear/', views.crear_panorama, name='crear_panorama'),
    path('panoramas/editar/<int:panorama_id>/', views.editar_panorama, name='editar_panorama'),
    path('panoramas/eliminar/<int:panorama_id>/', views.eliminar_panorama, name='eliminar_panorama'),

    # Panoramas informativos
    path('feria-emprendedores/', views.feria_emprendedores, name='feria_emprendedores'),
    path('feria-comida/', views.feria_comida, name='feria_comida'),
    path('concierto/', views.concierto, name='concierto'),
    path('trekking/', views.trekking, name='trekking'),

    # Consumo API externa (IL10)
    path('consumo-api/', views.consumo_api, name='consumo_api'),
]
