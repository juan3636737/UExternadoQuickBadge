from django.shortcuts import render
from .models import Personal
from .models import Carrusel


from .models import Personal, Carrusel, ProfesorDestacado  
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generar_pdf(request):
    # Creamos una respuesta HTTP con tipo de contenido 'application/pdf'
    response = HttpResponse(content_type='application/pdf')
    # Especificamos el encabezado Content-Disposition para que el navegador descargue el archivo como 'reporte.pdf'
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Creamos el objeto PDF, usando la respuesta HTTP como su "archivo".
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "¡Hola, mundo!")

    # Cerramos el objeto PDF de manera limpia.
    p.showPage()
    p.save()

    # Devolvemos la respuesta HTTP con el contenido del PDF generado
    return response
# views.py

# Asegúrate de importar ProfesorDestacado

def index(request):
    carrusel_items = Carrusel.objects.all()
    personal_items = Personal.objects.all()
    profesores_destacados = ProfesorDestacado.objects.all()  # Obtener todos los profesores destacados
    return render(request, 'index.html', {'carrusel_items': carrusel_items, 'personal_items': personal_items, 'profesores_destacados': profesores_destacados})


from django.shortcuts import render
from django.db.models import Sum
from .models import RegistroHoras, Profesor

from django.shortcuts import render
from .models import RegistroHoras

def consultar_horas_trabajadas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        documento = request.POST.get('documento')
        
        # Realizar la consulta en la base de datos
        try:
            profesor = Profesor.objects.get(nombre=nombre, documento_identidad=documento)
            horas_trabajadas = RegistroHoras.objects.filter(profesor=profesor).aggregate(total_horas=Sum('horas_trabajadas'))['total_horas']
        except Profesor.DoesNotExist:
            horas_trabajadas = None

        return render(request, 'resultado_horas_trabajadas.html', {'horas_trabajadas': horas_trabajadas})

    return render(request, 'formulario_consulta_horas.html')

from rest_framework import viewsets
from .models import (Facultad, Dependencia, Departamento, NivelRutaDocente, Duracion, Codigo, Nombreestrategia, Profesor, RegistroHoras, Carrusel, Personal, ProfesorDestacado, Dinamización_de_conocimiento, Diseño_de_Ambientes, Gestión_información, Gestión_proyectos, Gestión_conocimiento, Producción_de_recursos, Transversales)
from .serializers import (FacultadSerializer, DependenciaSerializer, DepartamentoSerializer, NivelRutaDocenteSerializer, DuracionSerializer, CodigoSerializer, NombreestrategiaSerializer, ProfesorSerializer, RegistroHorasSerializer, CarruselSerializer, PersonalSerializer, ProfesorDestacadoSerializer, Dinamización_de_conocimientoSerializer, Diseño_de_AmbientesSerializer, Gestión_informaciónSerializer, Gestión_proyectosSerializer, Gestión_conocimientoSerializer, Producción_de_recursosSerializer, TransversalesSerializer)

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class NivelRutaDocenteViewSet(viewsets.ModelViewSet):
    queryset = NivelRutaDocente.objects.all()
    serializer_class = NivelRutaDocenteSerializer

class DuracionViewSet(viewsets.ModelViewSet):
    queryset = Duracion.objects.all()
    serializer_class = DuracionSerializer

class CodigoViewSet(viewsets.ModelViewSet):
    queryset = Codigo.objects.all()
    serializer_class = CodigoSerializer

class NombreestrategiaViewSet(viewsets.ModelViewSet):
    queryset = Nombreestrategia.objects.all()
    serializer_class = NombreestrategiaSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class RegistroHorasViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoras.objects.all()
    serializer_class = RegistroHorasSerializer

class CarruselViewSet(viewsets.ModelViewSet):
    queryset = Carrusel.objects.all()
    serializer_class = CarruselSerializer

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class ProfesorDestacadoViewSet(viewsets.ModelViewSet):
    queryset = ProfesorDestacado.objects.all()
    serializer_class = ProfesorDestacadoSerializer

class Dinamización_de_conocimientoViewSet(viewsets.ModelViewSet):
    queryset = Dinamización_de_conocimiento.objects.all()
    serializer_class = Dinamización_de_conocimientoSerializer

class Diseño_de_AmbientesViewSet(viewsets.ModelViewSet):
    queryset = Diseño_de_Ambientes.objects.all()
    serializer_class = Diseño_de_AmbientesSerializer

class Gestión_informaciónViewSet(viewsets.ModelViewSet):
    queryset = Gestión_información.objects.all()
    serializer_class = Gestión_informaciónSerializer

class Gestión_proyectosViewSet(viewsets.ModelViewSet):
    queryset = Gestión_proyectos.objects.all()
    serializer_class = Gestión_proyectosSerializer

class Gestión_conocimientoViewSet(viewsets.ModelViewSet):
    queryset = Gestión_conocimiento.objects.all()
    serializer_class = Gestión_conocimientoSerializer

class Producción_de_recursosViewSet(viewsets.ModelViewSet):
    queryset = Producción_de_recursos.objects.all()
    serializer_class = Producción_de_recursosSerializer

class TransversalesViewSet(viewsets.ModelViewSet):
    queryset = Transversales.objects.all()
    serializer_class = TransversalesSerializer

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import RegistroHoras
from django.db.models import Sum

def update_registro_horas(request, registro_id):
    registro = get_object_or_404(RegistroHoras, id=registro_id)
    
    total_horas = 0
    related_fields = [
        registro.dinamizacion_de_redes_de_conocimiento,
        registro.diseño_de_ambientes_virtuales_de_aprendizaje,
        registro.gestion_de_la_informacion,
        registro.gestion_de_proyectos_con_TIC,
        registro.gestion_del_conocimiento_docente,
        registro.produccion_de_recursos_educativos_digitales,
        registro.transversales,
    ]
    
    for field in related_fields:
        total_horas += field.aggregate(total=Sum('duracion'))['total'] or 0
    
    registro.horas_trabajadas = total_horas
    registro.save()
    
    return HttpResponse(f"Total de horas trabajadas actualizadas: {registro.horas_trabajadas}")
