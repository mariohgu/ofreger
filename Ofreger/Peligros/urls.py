from django.urls import path
from Peligros import views

urlpatterns = [
    path("", views.PeligroListView.as_view(), name="peligro"),
    path("registro/", views.registro),
    path("cargarPdf/", views.cargarPdf),
    path("validarPdf/", views.validarPdf),
    # path("editarCurso/<int:id>", views.editarCurso),
]
