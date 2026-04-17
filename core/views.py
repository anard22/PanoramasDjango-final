from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User, Group

from .models import Perfil
from .forms import UsuarioForm, PerfilForm


# -------------------------
# Utilidades de roles
# -------------------------
def es_admin(user):
    return user.groups.filter(name='Administrador').exists()


# -------------------------
# Vistas públicas
# -------------------------
def home(request):
    return render(request, 'core/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'core/index.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def recuperar_contrasena(request):
    return render(request, 'core/recuperar.html')


# -------------------------
# Registro de usuario
# -------------------------
def registro(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            # Asignar grupo Cliente por defecto
            grupo_cliente, _ = Group.objects.get_or_create(name='Cliente')
            user.groups.add(grupo_cliente)

            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')

    else:
        user_form = UsuarioForm()
        perfil_form = PerfilForm()

    return render(request, 'core/registro.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })


# -------------------------
# Vistas protegidas
# -------------------------
@login_required
def perfil(request):
    return render(request, 'core/perfil.html')


@login_required
@user_passes_test(es_admin)
def admin_panel(request):
    return render(request, 'core/admin-panel.html')


@login_required
@user_passes_test(es_admin)
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'core/listar_usuarios.html', {
        'usuarios': usuarios
    })


@login_required
@user_passes_test(es_admin)
def crear_usuario(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            messages.success(request, 'Usuario creado correctamente')
            return redirect('listar_usuarios')

    else:
        user_form = UsuarioForm()
        perfil_form = PerfilForm()

    return render(request, 'core/crear_usuario.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })


# -------------------------
# Panoramas (solo render)
# -------------------------
def feria_emprendedores(request):
    return render(request, 'core/feria-emprendedores.html')


def feria_comida(request):
    return render(request, 'core/feria-comida.html')


def concierto(request):
    return render(request, 'core/concierto-parque.html')


def trekking(request):
    return render(request, 'core/trekking-quebrada.html')
