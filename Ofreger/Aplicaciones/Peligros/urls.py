from django.urls import path
from Aplicaciones.Peligros import views

urlpatterns = [
    path("", views.PeligroListView.as_view(), name="peligro"),
    path("registro/", views.registro),
    path("cargarPdf/", views.cargarPdf),
    path("validarPdf/", views.validarPdf),
    path("eliminarPeligro/<int:id>", views.eliminarPeligro),
    path("editarPeligro/<int:id>", views.editarPeligro),
    path("generacionTablas/", views.generacionTablas),
    path("tablas/", views.tablas),
    path("nuevo/", views.nuevo),
]