# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import update_registro_horas
from .views import (FacultadViewSet, DependenciaViewSet, DepartamentoViewSet, NivelRutaDocenteViewSet, DuracionViewSet, CodigoViewSet, NombreestrategiaViewSet, ProfesorViewSet, RegistroHorasViewSet, CarruselViewSet, PersonalViewSet, ProfesorDestacadoViewSet, Dinamización_de_conocimientoViewSet, Diseño_de_AmbientesViewSet, Gestión_informaciónViewSet, Gestión_proyectosViewSet, Gestión_conocimientoViewSet, Producción_de_recursosViewSet, TransversalesViewSet)

router = DefaultRouter()
router.register(r'facultad', FacultadViewSet)
router.register(r'dependencia', DependenciaViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'nivelruta', NivelRutaDocenteViewSet)
router.register(r'duracion', DuracionViewSet)
router.register(r'codigo', CodigoViewSet)
router.register(r'nombreestrategia', NombreestrategiaViewSet)
router.register(r'profesor', ProfesorViewSet)
router.register(r'registrohoras', RegistroHorasViewSet)
router.register(r'carrusel', CarruselViewSet)
router.register(r'personal', PersonalViewSet)
router.register(r'profesordestacado', ProfesorDestacadoViewSet)
router.register(r'dinamizacion', Dinamización_de_conocimientoViewSet)
router.register(r'disenoambientes', Diseño_de_AmbientesViewSet)
router.register(r'gestioninformacion', Gestión_informaciónViewSet)
router.register(r'gestionproyectos', Gestión_proyectosViewSet)
router.register(r'gestionconocimiento', Gestión_conocimientoViewSet)
router.register(r'produccionrecursos', Producción_de_recursosViewSet)
router.register(r'transversales', TransversalesViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('update_registro_horas/<int:registro_id>/', update_registro_horas, name='update_registro_horas'),
]
