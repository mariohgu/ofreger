from typing import Any
import os
from django.db.models.query import QuerySet
from .models import Peligro, Usuario
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .script import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

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
    return render(request, "registro.html")


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
            nuevo_peligro = Peligro.objects.create(
                sinpad=sinpad,
                provincia=items[0],
                distrito=items[1],
                localidad=items[2],
                ubigeo=items[3],
                latitud=items[4],
                longitud=items[5],
                descripcion=items[6],
                url_pdf=None,
            )

            # Guarda el archivo PDF en el campo 'url_pdf' y guarda la instancia
            nuevo_peligro.url_pdf.save(pdf_file.name, pdf_file, save=True)

            # Obtén la URL del archivo PDF
            pdf_url = nuevo_peligro.url_pdf.url

            id_nuevo = nuevo_peligro.id

            # Asigna los valores extraídos a las variables correspondientes
            id = id_nuevo
            provincia = items[0]
            distrito = items[1]
            localidad = items[2]
            ubigeo = items[3]
            latitud = items[4]
            longitud = items[5]
            descripcion = items[6]

    # Prepara el diccionario de datos para enviar al template
    data = {
        "id": id,
        "sinpad": sinpad,
        "provincia": provincia,
        "distrito": distrito,
        "localidad": localidad,
        "ubigeo": ubigeo,
        "latitud": latitud,
        "longitud": longitud,
        "descripcion": descripcion,
        "url_pdf": pdf_url,
    }

    # Si no es una solicitud POST, simplemente muestra el formulario
    return render(request, "registro.html", data)


def validarPdf(request):
    id = request.POST["id"]
    sinpad = request.POST["txtsinpad"]
    provincia = request.POST["txtprovincia"]
    distrito = request.POST["txtdistrito"]
    localidad = request.POST["txtlocalidad"]
    ubigeo = request.POST["txtubigeo"]
    latitud = request.POST["txtlatitud"]
    longitud = request.POST["txtlongitud"]
    descripcion = request.POST["txtdescripcion"]

    regis_peligro = Peligro.objects.get(id=id)
    regis_peligro.sinpad = sinpad
    regis_peligro.provincia = provincia
    regis_peligro.distrito = distrito
    regis_peligro.localidad = localidad
    regis_peligro.ubigeo = ubigeo
    regis_peligro.latitud = latitud
    regis_peligro.longitud = longitud
    regis_peligro.descripcion = descripcion
    regis_peligro.save()

    return redirect("/nuevo/")


def editarPeligro(request, id):
    peligro = Peligro.objects.get(id=id)
    # data = {"Titulo": "Edicion de Curso", "curso": curso}
    data = {
        "id": peligro.id,
        "sinpad": peligro.sinpad,
        "provincia": peligro.provincia,
        "distrito": peligro.distrito,
        "localidad": peligro.localidad,
        "ubigeo": peligro.ubigeo,
        "latitud": peligro.latitud,
        "longitud": peligro.longitud,
        "descripcion": peligro.descripcion,
        "url_pdf": peligro.url_pdf,
    }
    return render(request, "registro.html", data)


def eliminarPeligro(request, id):
    peligro = Peligro.objects.get(id=id)
    pdf_path = peligro.url_pdf.path
    if os.path.isfile(pdf_path):
        os.remove(pdf_path)
    peligro.delete()
    return redirect("/tablas/")


def generacionTablas(request):
    peligros = list(Peligro.objects.values())
    data = {"peligros": peligros}
    return JsonResponse(data)


def listasinpad(request):
    # Obtén todos los objetos Peligro y extrae solo el atributo 'sinpad'
    sinpad_values = list(Peligro.objects.values_list("sinpad", flat=True))
    data = {"sinpad": sinpad_values}
    return JsonResponse(data)


def registrarUsuario(request):
    Nombre = request.POST["txtNombre"]
    email = request.POST["txtEmail"]
    usuario = request.POST["txtUsuario"]
    clave = request.POST["txtClave"]

    nuevo_usuario = Usuario.objects.create(usuario=usuario, email=email, Nombre=Nombre)

    nuevo_usuario.set_password(clave)
    nuevo_usuario.save()

    return redirect("/crearUsuario/")


def logueo(request):
    if request.method == "POST":
        usuario = request.POST["txtUsuario"]
        clave = request.POST["txtClave"]

        username = Usuario.objects.filter(usuario=usuario, clave=clave).first()

        user = authenticate(username=usuario, password=clave)
        if username and username.check_password(clave):
            login(request, user)
            return redirect("/nuevo/")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("/login/")
    else:
        return redirect("/login/")


def crearUsuario(request):
    return render(request, "crearUsuario.html")


def tablas(request):
    return render(request, "tabla.html")


def nuevo(request):
    return render(request, "cargaPdf.html")


def login(request):
    return render(request, "login.html")
