from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Curso


# Create your views here.


def home(request):
    # curso = Curso.objects.all()[:5] #Estoy diciendo que solo quiero los 5 primeros, puedo jugar con los ordenamientos
    # curso = Curso.objects.all().order_by("-creditos") #con menos es el ordenamiento descendente
    # curso = Curso.objects.all().order_by("nombre", "-creditos")
    # curso = Curso.objects.filter(creditos=4) #Filtrado
    # curso = Curso.objects.filter(creditos__gt=4) #filtrado con mayores de 4

    curso = Curso.objects.all()
    return render(request, "cursosVista.html", {"cursos": curso})


class CursoListView(ListView):
    model = Curso
    template_name = "cursosVista.html"

    def get_queryset(self):
        return Curso.objects.all()
        # return Curso.objects.filter(creditos__lte=5)
        # return self.model.objects.filter(creditos__gt=4)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["Titulo"] = "Listado de Cursos"
        return context


def registrarCurso(request):
    nombre = request.POST["txtNombre"]
    creditos = request.POST["numCreditos"]
    registro = Curso.objects.create(nombre=nombre, creditos=creditos)

    return redirect("/")


def eliminarCurso(request, id):
    item = Curso.objects.get(id=id)
    item.delete()
    return redirect("/")


def editarCurso(request, id):
    curso = Curso.objects.get(id=id)
    data = {"Titulo": "Edicion de Curso", "curso": curso}
    return render(request, "editarCurso.html", data)


def editandoCurso(request):
    id = int(request.POST["id"])
    nombre = request.POST["txtNombre"]
    creditos = request.POST["numCreditos"]
    item = Curso.objects.get(id=id)
    item.nombre = nombre
    item.creditos = creditos
    item.save()
    return redirect("/")
