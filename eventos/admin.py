from django.contrib import admin
from .models import Evento, Inscripcion



class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 0
    readonly_fields = ("nombre", "correo", "cantidad", "creada")

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "lugar", "valor", "cupos", "disponibles", "activo")
    list_filter = ("activo", "lugar")
    search_fields = ("nombre", "lugar")
    list_editable = ("activo",)
    inlines = [InscripcionInline]

    @admin.display(description="Disponibles")
    def disponibles(self, obj):
        return obj.cupos_disponibles()
    
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "evento", "cantidad", "creada")
    list_filter = ("evento",)
    search_fields = ("nombre", "correo", "evento _nombre")
