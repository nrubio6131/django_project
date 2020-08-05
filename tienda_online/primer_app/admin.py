from django.contrib import admin
from primer_app.models import tabla,prueba

class tablaAdmin (admin.ModelAdmin):
    list_display = ("nombre","apellido","profesion","correo","edad","fecha_creacion","activo")
    search_fields = ("nombre","apellido")
    list_filter = ("edad","fecha_creacion","activo")
    date_hierarchy = "fecha_creacion"


admin.site.register(tabla,tablaAdmin)
admin.site.register(prueba)
# Register your models here.
