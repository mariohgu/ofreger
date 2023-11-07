from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = f"{self.nombre} ({self.creditos})"

        return texto
