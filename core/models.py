from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    """
    Modelo que extiende al usuario de Django con información adicional.
    Los roles se gestionan mediante Groups (Administrador, Cliente, Operador),
    no desde este modelo.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


# ==========================
# MODELO DE NEGOCIO (CRUD)
# ==========================
class Panorama(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

