from typing import Any
from django.db.models.query import QuerySet
from .models import Peligro
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .script import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.


class PeligroListView(ListView):
    model = Peligro
    template_name = "cargaPdf.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Peligro.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["Titulo"] = "Registrar Peligro"
        return context


def registro(request):
    txtsinpad = request.POST["txtsinpad"]
    txtprovincia = request.POST["txtprovincia"]
    txtdistrito = request.POST["txtdistrito"]
    txtlocalidad = request.POST["txtlocalidad"]
    txtubigeo = request.POST["txtubigeo"]
    txtlatitud = request.POST["txtlatitud"]
    txtlongitud = request.POST["txtlongitud"]
    txtdescripcion = request.POST["txtdescripcion"]
    url_pdf = request.POST["url_pdf"]
    carga = Peligro.objects.create(
        sinpad=txtsinpad,
        provincia=txtprovincia,
        distrito=txtdistrito,
        localidad=txtlocalidad,
        ubigeo=txtubigeo,
        latitud=txtlatitud,
        longitud=txtlongitud,
        descripcion=txtdescripcion,
        url_pdf=url_pdf,
    )

    return redirect("/")


from django.shortcuts import render
from .models import Peligro


def cargarPdf(request):
    # Inicializa las variables para evitar errores si no son establecidas
    sinpad = (
        provincia
    ) = (
        distrito
    ) = localidad = ubigeo = latitud = longitud = descripcion = pdf_url = None

    if request.method == "POST":
        # Obtén el número de SINPAD del formulario
        sinpad = request.POST["txtsinpad"]

        # Obtén el archivo PDF del formulario
        pdf_file = request.FILES.get("pdf")

        if pdf_file:
            # Procesa el PDF
            items = process_pdf(pdf_file)

            # Crea una nueva instancia del modelo Peligro y asigna los valores
            nuevo_peligro = Peligro(
                sinpad=sinpad,
                provincia=items[0],
                distrito=items[1],
                localidad=items[2],
                ubigeo=items[3],
                latitud=items[4],
                longitud=items[5],
                descripcion=items[6],
                # Asegúrate de que 'url_pdf' sea el nombre de tu FileField en el modelo
                url_pdf=None,
            )

            # Guarda el archivo PDF en el campo 'url_pdf' y guarda la instancia
            nuevo_peligro.url_pdf.save(pdf_file.name, pdf_file, save=True)

            # Obtén la URL del archivo PDF
            pdf_url = nuevo_peligro.url_pdf.url

            # Asigna los valores extraídos a las variables correspondientes
            provincia = items[0]
            distrito = items[1]
            localidad = items[2]
            ubigeo = items[3]
            latitud = items[4]
            longitud = items[5]
            descripcion = items[6]

    # Prepara el diccionario de datos para enviar al template
    data = {
        "sinpad": sinpad,
        "provincia": provincia,
        "distrito": distrito,
        "localidad": localidad,
        "ubigeo": ubigeo,
        "latitud": latitud,
        "longitud": longitud,
        "descripcion": descripcion,
        "pdf_url": pdf_url,  # Esta será la URL para acceder al archivo PDF
    }

    # Si no es una solicitud POST, simplemente muestra el formulario
    return render(request, "registro.html", data)
