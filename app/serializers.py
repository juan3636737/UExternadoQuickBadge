from rest_framework import serializers
from .models import (Facultad, Dependencia, Departamento, NivelRutaDocente, Duracion, Codigo, Nombreestrategia, Profesor,  RegistroHoras, Carrusel, Personal, ProfesorDestacado, Dinamización_de_conocimiento, Diseño_de_Ambientes, Gestión_información, Gestión_proyectos, Gestión_conocimiento, Producción_de_recursos, Transversales)

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class NivelRutaDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelRutaDocente
        fields = '__all__'

class DuracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duracion
        fields = '__all__'

class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codigo
        fields = '__all__'

class NombreestrategiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nombreestrategia
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class Dinamización_de_conocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinamización_de_conocimiento
        fields = '__all__'

class Diseño_de_AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseño_de_Ambientes
        fields = '__all__'
        
class Gestión_informaciónSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestión_información
        fields = '__all__'
    
class Gestión_proyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestión_proyectos
        fields = '__all__'        
        
class Gestión_conocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestión_conocimiento
        fields = '__all__'  
        
class Producción_de_recursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producción_de_recursos
        fields = '__all__'     

class TransversalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transversales
        fields = '__all__'  
              
class RegistroHorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoras
        fields = '__all__'

class CarruselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrusel
        fields = '__all__'

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class ProfesorDestacadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesorDestacado
        fields = '__all__'
