from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class Peligro(models.Model):
    sinpad = models.IntegerField()
    provincia = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    ubigeo = models.IntegerField()
    latitud = models.CharField(max_length=15, null=True, blank=True)
    longitud = models.CharField(max_length=15, null=True, blank=True)
    descripcion = models.TextField()
    url_pdf = models.FileField(upload_to="peligros_pdfs/", null=True, blank=True)

    class Meta:
        verbose_name = "Peligro"
        verbose_name_plural = "Peligros"
        db_table = "peligro"


class Usuario(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    clave = models.CharField(max_length=128)
    email = models.CharField(max_length=50, unique=True)
    Nombre = models.CharField(max_length=50, null=True, blank=True)

    def set_password(self, password):
        self.clave = make_password(password)

    def check_password(self, password):
        return check_password(self.clave, password)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "usuario"


# class Curso(models.Model):
#     nombre = models.CharField(max_length=50)
#     creditos = models.PositiveSmallIntegerField()
#     docente = models.ForeignKey(
#         Docente, null=True, blank=True, on_delete=models.CASCADE
#     )
