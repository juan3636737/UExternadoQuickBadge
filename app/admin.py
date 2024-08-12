from django.contrib import admin
from django.http import HttpResponse
import openpyxl
from .models import (
    Facultad, Dependencia, Carrusel, Codigo, ProfesorDestacado, Personal, RegistroHoras, 
    Transversales, Departamento, Producción_de_recursos, NivelRutaDocente, Duracion, Profesor, 
    Gestión_conocimiento, Nombreestrategia, Dinamización_de_conocimiento, Diseño_de_Ambientes, 
    Gestión_información, Gestión_proyectos
)
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from .forms import RegistroHorasForm
from .filters import (
    NivelDinamizacionRedesFilter, 
    NivelDisenoAmbientesFilter,
    NivelGestionInformacionFilter,
    NivelGestionProyectosFilter,
    NivelGestionConocimientoFilter,
    NivelProduccionRecursosFilter,
    NivelTransversalesFilter,
)
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = 'Gestión Fofo'
    site_title = 'Gestión Fofo Admin'
    index_title = 'Bienvenido al panel de administración de Gestión Fofo'

admin_site = MyAdminSite(name='myadmin')

# Definición del filtro NivelFilter
class NivelFilter(SimpleListFilter):
    title = _('Nivel final')
    parameter_name = 'nivel'

    def lookups(self, request, model_admin):
        return (
            ('inicial', _('Inicial o Explorador')),
            ('intermedio', _('Intermedio o Integrador')),
            ('avanzado', _('Avanzado o Innovador')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_trabajadas__gte=120, horas_trabajadas__lte=240)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_trabajadas__gt=240, horas_trabajadas__lte=360)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_trabajadas__gt=360)
        return queryset

# Acción para exportar a Excel (reporte open badge)
@admin.action(description='Exportar a Excel (reporte open badge)')





# Registro de la clase RegistroHorasAdmin
class RegistroHorasAdmin(admin.ModelAdmin):
    form = RegistroHorasForm
    actions = ['exportar_excel', 'exportar_open_badge', 'alternar_sumar_restar_horas']
    list_display = ('profesor', 'mostrar_facultades', 'mostrar_departamento', 'mostrar_dependencia', 'horas_trabajadas', 'get_nivel')
    search_fields = ['profesor__nombre', 'profesor__apellido', 'profesor__documento_identidad']
    list_filter = (
        'profesor__documento_identidad',
        'profesor__facultad',
        'profesor__dependencia',
        'profesor__departamento',
        'horas_trabajadas',
        NivelFilter,
        NivelDinamizacionRedesFilter,
        NivelDisenoAmbientesFilter,
        NivelGestionInformacionFilter,
        NivelGestionProyectosFilter,
        NivelGestionConocimientoFilter,
        NivelProduccionRecursosFilter,
        NivelTransversalesFilter,
    )
    fieldsets = (
        (None, {
            'fields': (
                'profesor',
            )
        }),
        ('Competencias', {
            'fields': (
                'dinamizacion_de_redes_de_conocimiento',
                'diseño_de_ambientes_virtuales_de_aprendizaje',
                'gestion_de_la_informacion',
                'gestion_de_proyectos_con_TIC',
                'gestion_del_conocimiento_docente',
                'produccion_de_recursos_educativos_digitales',
                'transversales',
            )
        }),
        ('Horas y Niveles', {
            'fields': (
                ('horas_dinamizacion_redes_insignia', 'nivel_dinamizacion_redes'),
                ('horas_diseno_ambientes_insignia', 'nivel_diseno_ambientes'),
                ('horas_gestion_informacion_insignia', 'nivel_gestion_informacion'),
                ('horas_gestion_proyectos_insignia', 'nivel_gestion_proyectos'),
                ('horas_gestion_conocimiento_insignia', 'nivel_gestion_conocimiento'),
                ('horas_produccion_recursos_insignia', 'nivel_produccion_recursos'),
                ('horas_transversales_insignia', 'nivel_transversales'),
            )
        }),
        ('Acumuladores y Otros', {
            'fields': (
                'acomulador_dinamizacion_redes',
                'acomulador_diseno_ambientes',
                'acomulador_gestion_informacion',
                'acomulador_gestion_proyectos',
                'acomulador_gestion_conocimiento',
                'acomulador_produccion_recursos',
                'acomulador_transversales',
                'horas_trabajadas',
                'nivel',
            )
        }),
    )


        

    
    def exportar_open_badge(modeladmin, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Reporte Open Badge insignia de nivel"

        headers = ['Correo Electrónico', 'Nombre ']
        ws.append(headers)

        for registro in queryset:
            profesor = registro.profesor
            ws.append([
                profesor.correo_electronico,
                profesor.nombre_completo
            ])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=reporte_open_badge.xlsx'
        wb.save(response)
        return response
    exportar_open_badge.short_description = "Exportar Open Badge insiginia de nivel"

    def exportar_excel(modeladmin, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Registros de Horas"
        headers = [
            'Nombre', 'Apellido', 'Documento Identidad', 
            'Correo Electrónico', 'Facultad', 'Dependencia', 'Departamento', 
            'Dinamización de Redes de Conocimiento', 'Diseño de Ambientes Virtuales de Aprendizaje', 
            'Gestión de la Información', 'Gestión de Proyectos con TIC', 'Gestión del Conocimiento Docente', 
            'Producción de Recursos Educativos Digitales', 'Transversales', 
            'Horas Trabajadas', 'Nivel'
        ]
        ws.append(headers)

        for registro in queryset:
            profesor = registro.profesor
            ws.append([
            profesor.nombre, profesor.apellido, profesor.documento_identidad, 
            profesor.correo_electronico,
            ', '.join([facultad.nombre for facultad in profesor.facultad.all()]),
            profesor.dependencia.nombre,
            profesor.departamento.nombre,
            ', '.join([str(e) for e in registro.dinamizacion_de_redes_de_conocimiento.all()]),
            ', '.join([str(e) for e in registro.diseño_de_ambientes_virtuales_de_aprendizaje.all()]),
            ', '.join([str(e) for e in registro.gestion_de_la_informacion.all()]),
            ', '.join([str(e) for e in registro.gestion_de_proyectos_con_TIC.all()]),
            ', '.join([str(e) for e in registro.gestion_del_conocimiento_docente.all()]),
            ', '.join([str(e) for e in registro.produccion_de_recursos_educativos_digitales.all()]),
            ', '.join([str(e) for e in registro.transversales.all()]),
            registro.horas_trabajadas,
            registro.get_nivel()
        ])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=registros_horas.xlsx'
        wb.save(response)
        return response

    def alternar_sumar_restar_horas(modeladmin, request, queryset):
        last_state = request.session.get('sumar_restar_last_state', True)

        for registro in queryset:
            cambio_horas = 15 if last_state else -15
            registro.horas_trabajadas += cambio_horas
            registro.save()

        request.session['sumar_restar_last_state'] = not last_state
        accion = "Sumar" if last_state else "Restar"
        modeladmin.message_user(request, f"Se han {accion} 15 horas para {queryset.count()} registros.")

    
    def profesor_documento_identidad(self, obj):
        return obj.profesor.documento_identidad
    profesor_documento_identidad.short_description = 'Documento Identidad Profesor'


    def mostrar_facultades(self, obj):
        return ", ".join([facultad.nombre for facultad in obj.profesor.facultad.all()])
    mostrar_facultades.short_description = 'Facultades'

    def mostrar_departamento(self, obj):
        return obj.profesor.departamento.nombre
    mostrar_departamento.short_description = 'Departamento'

    def mostrar_dependencia(self, obj):
        return obj.profesor.dependencia.nombre
    mostrar_dependencia.short_description = 'Dependencia'
    def get_nivel(self, obj):
        return obj.get_nivel()
    get_nivel.short_description = 'Nivel'

admin.site.register(RegistroHoras, RegistroHorasAdmin)

# Registro de otros modelos
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento_identidad', 'correo_electronico', 'dependencia', 'departamento', 'mostrar_facultades')
    list_filter = ('facultad', 'dependencia', 'departamento')
    search_fields = ('nombre', 'apellido', 'documento_identidad')


    def mostrar_facultades(self, obj):
        return ", ".join([facultad.nombre for facultad in obj.facultad.all()])
    mostrar_facultades.short_description = 'Facultades'

# Otras clases admin para los modelos
@admin.register(Dinamización_de_conocimiento)
class Dinamización_de_conocimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre_estrategia_capacitacion', 'codigo', 'fecha_inicio', 'fecha_fin', 'nivel_ruta_docente', 'duracion')
    list_filter = ('nivel_ruta_docente', 'duracion', 'codigo')

@admin.register(Diseño_de_Ambientes)
class Diseño_de_AmbientesAdmin(admin.ModelAdmin):
    list_display = ('nombre_estrategia_capacitacion', 'codigo', 'fecha_inicio', 'fecha_fin', 'nivel_ruta_docente', 'duracion')
    list_filter = ('nivel_ruta_docente', 'duracion', 'codigo')

@admin.register(Gestión_información)
class Gestión_informaciónAdmin(admin.ModelAdmin):
    list_display = ('nombre_estrategia_capacitacion', 'codigo', 'fecha_inicio', 'fecha_fin', 'nivel_ruta_docente', 'duracion')
    list_filter = ('nivel_ruta_docente', 'duracion', 'codigo')

@admin.register(Gestión_proyectos)
class Gestión_proyectosAdmin(admin.ModelAdmin):
    list_display = ('nombre_estrategia_capacitacion', 'codigo', 'fecha_inicio', 'fecha_fin', 'nivel_ruta_docente', 'duracion')
    list_filter = ('nivel_ruta_docente', 'duracion', 'codigo')

@admin.register(Gestión_conocimiento)
class Gestión_conocimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre_estrategia_capacitacion', 'codigo', 'fecha_inicio', 'fecha_fin', 'nivel_ruta_docente', 'duracion')
    list_filter = ('nivel_ruta_docente', 'duracion', 'codigo')

@admin.register(Transversales)
class TransversalesAdmin(admin.ModelAdmin):
    list_display = ('nombre_estrategia_capacitacion', 'codigo', 'fecha_inicio', 'fecha_fin', 'nivel_ruta_docente', 'duracion')
    list_filter = ('nivel_ruta_docente', 'duracion', 'codigo')

@admin.register(Producción_de_recursos)
class Producción_de_recursosAdmin(admin.ModelAdmin):
    list_display = ('nombre_estrategia_capacitacion', 'codigo', 'fecha_inicio', 'fecha_fin', 'nivel_ruta_docente', 'duracion')
    list_filter = ('nivel_ruta_docente', 'duracion', 'codigo')

# Registro de otros modelos
admin.site.register(Facultad)
admin.site.register(Dependencia)
admin.site.register(Carrusel)
admin.site.register(Codigo)
admin.site.register(ProfesorDestacado)
admin.site.register(Personal)
admin.site.register(Departamento)
admin.site.register(NivelRutaDocente)
admin.site.register(Duracion)
admin.site.register(Nombreestrategia)
