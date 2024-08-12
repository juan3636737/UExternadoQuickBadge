from django.contrib import admin
from .models import RegistroHoras

class NivelDinamizacionRedesFilter(admin.SimpleListFilter):
    title = 'Nivel Dinamización de Redes'
    parameter_name = 'nivel_dinamizacion_redes'

    def lookups(self, request, model_admin):
        return (
            ('inicial', 'Inicial o Explorador'),
            ('intermedio', 'Intermedio o Integrador'),
            ('avanzado', 'Avanzado o Innovador'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_dinamizacion_redes_insignia__gte=20, horas_dinamizacion_redes_insignia__lte=40)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_dinamizacion_redes_insignia__gt=40, horas_dinamizacion_redes_insignia__lte=50)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_dinamizacion_redes_insignia__gt=50)
        return queryset

class NivelDisenoAmbientesFilter(admin.SimpleListFilter):
    title = 'Nivel Diseño de Ambientes'
    parameter_name = 'nivel_diseno_ambientes'

    def lookups(self, request, model_admin):
        return (
            ('inicial', 'Inicial o Explorador'),
            ('intermedio', 'Intermedio o Integrador'),
            ('avanzado', 'Avanzado o Innovador'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_diseno_ambientes_insignia__gte=45, horas_diseno_ambientes_insignia__lte=90)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_diseno_ambientes_insignia__gt=90, horas_diseno_ambientes_insignia__lte=100)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_diseno_ambientes_insignia__gt=100)
        return queryset

class NivelGestionInformacionFilter(admin.SimpleListFilter):
    title = 'Nivel Gestión de Información'
    parameter_name = 'nivel_gestion_informacion'

    def lookups(self, request, model_admin):
        return (
            ('inicial', 'Inicial o Explorador'),
            ('intermedio', 'Intermedio o Integrador'),
            ('avanzado', 'Avanzado o Innovador'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_gestion_informacion_insignia__gte=20, horas_gestion_informacion_insignia__lte=40)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_gestion_informacion_insignia__gt=40, horas_gestion_informacion_insignia__lte=50)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_gestion_informacion_insignia__gt=50)
        return queryset

class NivelGestionProyectosFilter(admin.SimpleListFilter):
    title = 'Nivel Gestión de Proyectos'
    parameter_name = 'nivel_gestion_proyectos'

    def lookups(self, request, model_admin):
        return (
            ('inicial', 'Inicial o Explorador'),
            ('intermedio', 'Intermedio o Integrador'),
            ('avanzado', 'Avanzado o Innovador'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_gestion_proyectos_insignia__gte=120, horas_gestion_proyectos_insignia__lte=240)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_gestion_proyectos_insignia__gt=240, horas_gestion_proyectos_insignia__lte=350)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_gestion_proyectos_insignia__gt=350)
        return queryset

class NivelGestionConocimientoFilter(admin.SimpleListFilter):
    title = 'Nivel Gestión de Conocimiento'
    parameter_name = 'nivel_gestion_conocimiento'

    def lookups(self, request, model_admin):
        return (
            ('inicial', 'Inicial o Explorador'),
            ('intermedio', 'Intermedio o Integrador'),
            ('avanzado', 'Avanzado o Innovador'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_gestion_conocimiento_insignia__gte=20, horas_gestion_conocimiento_insignia__lte=40)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_gestion_conocimiento_insignia__gt=40, horas_gestion_conocimiento_insignia__lte=60)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_gestion_conocimiento_insignia__gt=60)
        return queryset

class NivelProduccionRecursosFilter(admin.SimpleListFilter):
    title = 'Nivel Producción de Recursos'
    parameter_name = 'nivel_produccion_recursos'

    def lookups(self, request, model_admin):
        return (
            ('inicial', 'Inicial o Explorador'),
            ('intermedio', 'Intermedio o Integrador'),
            ('avanzado', 'Avanzado o Innovador'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_produccion_recursos_insignia__gte=35, horas_produccion_recursos_insignia__lte=70)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_produccion_recursos_insignia__gt=70, horas_produccion_recursos_insignia__lte=80)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_produccion_recursos_insignia__gt=80)
        return queryset

class NivelTransversalesFilter(admin.SimpleListFilter):
    title = 'Nivel Transversales'
    parameter_name = 'nivel_transversales'

    def lookups(self, request, model_admin):
        return (
            ('inicial', 'Inicial o Explorador'),
            ('intermedio', 'Intermedio o Integrador'),
            ('avanzado', 'Avanzado o Innovador'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'inicial':
            return queryset.filter(horas_transversales_insignia__gte=120, horas_transversales_insignia__lte=240)
        elif self.value() == 'intermedio':
            return queryset.filter(horas_transversales_insignia__gt=240, horas_transversales_insignia__lte=350)
        elif self.value() == 'avanzado':
            return queryset.filter(horas_transversales_insignia__gt=350)
        return queryset
