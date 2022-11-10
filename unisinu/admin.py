from django.contrib import admin
from unisinu.models import *


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'password')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'email')



@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('codestudiantil', 'prinombre', 'priapellido', 'celular', 'estado')
    search_fields = ('nomcompleto', 'codestudiantil')
    list_filter = ('codestudiantil', 'codescuela')


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'codprestamista', 'codpretador', 'fechasolicitud', 'estado')
    search_fields = ('çodigo',)
    list_filter = ('fechasolicitud',)


@admin.register(Detalleprestamo)
class DetallePrestamoAdmin(admin.ModelAdmin):
    list_display = ('codprestamo', 'codutil', 'cantidad', 'fechauso')
    search_fields = ('codprestamo',)
    list_filter = ('fechauso',)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'fechainicio', 'fechafin')
    search_fields = ('codigo',)
    list_filter = ('fechainicio', 'fechafin',)