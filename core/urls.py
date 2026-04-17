from django.urls import path
from . import views

urlpatterns = [
    # Públicas
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('recuperar/', views.recuperar_contrasena, name='recuperar'),

    # Usuario
    path('perfil/', views.perfil, name='perfil'),

    # Administración (protegidas por rol)
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),

    # Panoramas
    path('feria-emprendedores/', views.feria_emprendedores, name='feria_emprendedores'),
    path('feria-comida/', views.feria_comida, name='feria_comida'),
    path('concierto/', views.concierto, name='concierto'),
    path('trekking/', views.trekking, name='trekking'),
]