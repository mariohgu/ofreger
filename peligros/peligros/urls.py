"""
URL configuration for peligros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from peligros import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bienvenida/", views.bienvenida),
    path("bienvenida123/", views.bienvenidaRojo),
    path("edad/<int:edad>/", views.categoriaEdad),
    path("fecha/", views.obtenermomentoactual),
    path("contenido/<str:nombre>/<int:edad>/", views.contenidoHTML),
    path("miprimeraplantilla/", views.miPrimeraPlantilla),
    path("plantillaparametros/", views.plantillaParametros),
    path("plantillacargador/", views.plantillaCargador),
    path("plantillaShortcut/", views.plantillaShortcut),
    path("plantillahija1/", views.plantillaHija1),
    path("plantillahija2/", views.plantillaHija2),
]
