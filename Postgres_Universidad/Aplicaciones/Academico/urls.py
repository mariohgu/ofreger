from django.urls import path
from Aplicaciones.Academico import views


urlpatterns = [
    path("", views.CursoListView.as_view(), name="gestion_cursos"),
    # path("editarCurso/<int:id>", views.editarCurso),
    path("eliminarCurso/<int:id>", views.eliminarCurso),
    path("registrarCurso/", views.registrarCurso),
    path("editarCurso/<int:id>", views.editarCurso),
    path("editandoCurso/", views.editandoCurso),
]
