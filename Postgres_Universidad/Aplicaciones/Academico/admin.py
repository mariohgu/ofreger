from django.contrib import admin
from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "creditos"]
    # ordering = ("-nombre", "creditos")
    # search_fields = ("nombre", "creditos")
    # list_editable = ("nombre",)
    # list_per_page = 3
    list_filter = ("creditos",)
    exclude = ("creditos",)  # restringo que se pueda modificar los creditos


# Register your models here.
# admin.site.register(Curso, CursoAdmin)
