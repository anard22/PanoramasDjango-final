from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User, Group

from .models import Perfil, Panorama
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
    if request.user.is_authenticated:
        return redirect('home')

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

    return render(request, 'core/registro.html')


# -------------------------
# Perfil (EDITABLE REAL)
# -------------------------
@login_required
def perfil(request):
    if request.method == "POST":
        perfil = request.user.perfil
        perfil.telefono = request.POST.get("telefono")
        perfil.direccion = request.POST.get("direccion")
        perfil.save()
        messages.success(request, "Perfil actualizado correctamente")

    return render(request, 'core/perfil.html')


# -------------------------
# Administración
# -------------------------
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
# CRUD DE PANORAMAS
# -------------------------
@login_required
def listar_panoramas(request):
    panoramas = Panorama.objects.all()
    return render(request, 'core/listar_panoramas.html', {
        'panoramas': panoramas
    })


@login_required
def crear_panorama(request):
    if request.method == 'POST':
        Panorama.objects.create(
            titulo=request.POST.get('titulo'),
            descripcion=request.POST.get('descripcion'),
            fecha=request.POST.get('fecha'),
            lugar=request.POST.get('lugar'),
            creador=request.user
        )
        messages.success(request, 'Panorama creado correctamente')
        return redirect('listar_panoramas')

    return render(request, 'core/crear_panorama.html')


@login_required
def editar_panorama(request, panorama_id):
    panorama = Panorama.objects.get(id=panorama_id)

    if request.method == 'POST':
        panorama.titulo = request.POST.get('titulo')
        panorama.descripcion = request.POST.get('descripcion')
        panorama.fecha = request.POST.get('fecha')
        panorama.lugar = request.POST.get('lugar')
        panorama.save()
        messages.success(request, 'Panorama actualizado correctamente')
        return redirect('listar_panoramas')

    return render(request, 'core/editar_panorama.html', {
        'panorama': panorama
    })


@login_required
def eliminar_panorama(request, panorama_id):
    panorama = Panorama.objects.get(id=panorama_id)
    panorama.delete()
    messages.success(request, 'Panorama eliminado correctamente')
    return redirect('listar_panoramas')


# -------------------------
# Panoramas informativos
# -------------------------
def feria_emprendedores(request):
    return render(request, 'core/feria-emprendedores.html')


def feria_comida(request):
    return render(request, 'core/feria-comida.html')


def concierto(request):
    return render(request, 'core/concierto-parque.html')


def trekking(request):
    return render(request, 'core/trekking-quebrada.html')

@login_required
def consumo_api(request):
    return render(request, 'core/consumo_api.html')