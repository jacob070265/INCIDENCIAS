from django.contrib import admin
from .models import Linea, Estacion, Incidencia

# Register your models here.

class EstacionInline(admin.StackedInline):
    model = Estacion
    
class LineaAdmin(admin.ModelAdmin): 
    inlines = [EstacionInline]
    list_display = ('nombre', 'color', 'distancia')
    
class IncidenteAdmin(admin.ModelAdmin): 
    list_display = ('texto', 'fecha')
    list_filter = ['fecha']

admin.site.register(Linea, LineaAdmin)
admin.site.register(Estacion)
admin.site.register(Incidencia, IncidenteAdmin)