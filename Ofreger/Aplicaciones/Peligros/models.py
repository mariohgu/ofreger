from django.db import models

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
    url_pdf = models.FileField(
        upload_to="peligros_pdfs/", null=True, blank=True
    )  # Aquí cambiamos url_pdf por pdf

    class Meta:
        verbose_name = "Peligro"
        verbose_name_plural = "Peligros"
        db_table = "peligro"
