from django.shortcuts import render
from .models import Curso

# Create your views here.


def home(request):
    curso = Curso.objects.all()
    return render(request, "cursosVista.html", {"cursos": curso})
