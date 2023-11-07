from django.contrib import admin
from .models import Curso, Docente


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ["id", "coloreado", "creditos"]
    # ordering = ("-nombre", "creditos")
    # search_fields = ("nombre", "creditos")
    # list_editable = ("nombre",)
    # list_per_page = 3
    # list_filter = ("creditos",)
    # list_display_links = ["id", "datos"]
    # exclude = ("creditos",)  # restringo que se pueda modificar los creditos

    # fieldsets = (
    #     (
    #         "Datos del Curso",
    #         {
    #             "fields": ("nombre",),
    #         },
    #     ),
    #     (
    #         "Otros Datos",
    #         {
    #             "classes": ("collapse", "wide", "extrapretty"),
    #             "fields": ("creditos",),
    #         },
    #     ),
    # )

    def datos(self, obj):
        return obj.nombre.upper()

    datos.short_description = "CURSO EN MAYUS"
    datos.empty_value_display = "???"
    datos.admin_order_field = "nombre"


# Register your models here.
# admin.site.register(Curso, CursoAdmin)

admin.site.register(Docente)
