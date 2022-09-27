from django.contrib import admin
from .models import Proyectos,Correos
# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):

    list_display= (
        "titulo",
        "imagen",
        "descripcion",
    )



admin.site.register(Proyectos,ProyectoAdmin)
admin.site.register(Correos)