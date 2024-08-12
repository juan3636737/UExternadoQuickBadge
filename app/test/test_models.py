from django.test import TestCase
from datetime import date  # Asegúrate de importar date desde datetime
from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError  # Add this import
from app.models import NivelRutaDocente, Duracion, Codigo, Nombreestrategia, Facultad, Dependencia, Departamento, Profesor, EstrategiaCapacitacion
from datetime import timedelta



        
class EstrategiaCapacitacionModelTestCase(TestCase):
    def setUp(self):
        self.nombre_estrategia = Nombreestrategia.objects.create(nombre="Estrategia A")
        self.codigo = Codigo.objects.create(numero="12345")
        self.nivel_ruta_docente = NivelRutaDocente.objects.create(nombre="Nivel Básico")

        self.estrategia = EstrategiaCapacitacion.objects.create(
            nombre_estrategia=self.nombre_estrategia,
            dependencia_digital='Dinamización de redes de conocimiento',
            codigo=self.codigo,
            nivel_ruta_docente=self.nivel_ruta_docente,
            fecha_inicio=date(2024, 1, 1),
            fecha_fin=date(2024, 1, 10),
            duracion=10,  # Duration in hours
            estado='VACIO',
            periodo='I',
            anio=2024
        )

    def test_estrategia_str(self):
        self.assertEqual(str(self.estrategia), "Estrategia A - 2024")

    def test_estado_choices(self):
        self.estrategia.estado = 'AP'
        self.estrategia.save()
        self.assertEqual(self.estrategia.estado, 'AP')

    def test_dependencia_digital_choices(self):
        self.estrategia.dependencia_digital = 'Gestión del conocimiento docente'
        self.estrategia.save()
        self.assertEqual(self.estrategia.dependencia_digital, 'Gestión del conocimiento docente')

    def test_periodo_choices(self):
        self.estrategia.periodo = 'II'
        self.estrategia.save()
        self.assertEqual(self.estrategia.periodo, 'II')

    def test_fecha_inicio_fecha_fin(self):
        self.assertEqual(self.estrategia.fecha_inicio, date(2024, 1, 1))
        self.assertEqual(self.estrategia.fecha_fin, date(2024, 1, 10))

    def test_duracion(self):
        self.assertEqual(self.estrategia.duracion, 10)

    def test_anio(self):
        self.assertEqual(self.estrategia.anio, 2024)

# Combine this with your existing tests
class CombinedModelsTestCase(TestCase):
    def setUp(self):
        # Initial set of models
        self.nivel_ruta_docente = NivelRutaDocente.objects.create(nombre="Nivel Básico")
        self.duracion = Duracion.objects.create(duracion=timedelta(hours=1, minutes=30))  # Duración de 1 hora y 30 minutos
        self.codigo = Codigo.objects.create(numero="12345")
        self.nombre_estrategia = Nombreestrategia.objects.create(nombre="Estrategia A")
        
        # Additional set of models
        self.facultad = Facultad.objects.create(nombre="Facultad de Ciencias")
        self.dependencia = Dependencia.objects.create(nombre="Dependencia de Matemáticas")
        self.departamento = Departamento.objects.create(nombre="Departamento de Álgebra")

        # Profesor model setup
        self.profesor = Profesor.objects.create(
            nombre="NombreCon50CaracteresExactamente" * 2,  # 50 characters
            apellido="Apellido Largos",
            documento_identidad="1234567890",
            correo_electronico="profesor@universidad.com",
            dependencia=self.dependencia,
            departamento=self.departamento
        )
        self.profesor.facultad.add(self.facultad)

        # EstrategiaCapacitacion model setup
        self.estrategia = EstrategiaCapacitacion.objects.create(
            nombre_estrategia=self.nombre_estrategia,
            dependencia_digital='Dinamización de redes de conocimiento',
            codigo=self.codigo,
            nivel_ruta_docente=self.nivel_ruta_docente,
            fecha_inicio=date(2024, 1, 1),
            fecha_fin=date(2024, 1, 10),
            duracion=10,  # Duration in hours
            estado='VACIO',
            periodo='I',
            anio=2024
        )

    def test_nivel_ruta_docente_str(self):
        nivel_ruta_docente = NivelRutaDocente.objects.get(id=self.nivel_ruta_docente.id)
        self.assertEqual(str(nivel_ruta_docente), "Nivel Básico")

    def test_duracion(self):
        duracion = Duracion.objects.get(id=self.duracion.id)
        self.assertEqual(str(duracion.duracion), "1:30:00")

    def test_codigo_str(self):
        codigo = Codigo.objects.get(id=self.codigo.id)
        self.assertEqual(str(codigo), "12345")

    def test_nombre_estrategia_str(self):
        nombre_estrategia = Nombreestrategia.objects.get(id=self.nombre_estrategia.id)
        self.assertEqual(str(nombre_estrategia), "Estrategia A")
        
    def test_facultad_str(self):
        facultad = Facultad.objects.get(id=self.facultad.id)
        self.assertEqual(str(facultad), "Facultad de Ciencias")

    def test_dependencia_str(self):
        dependencia = Dependencia.objects.get(id=self.dependencia.id)
        self.assertEqual(str(dependencia), "Dependencia de Matemáticas")

    def test_departamento_str(self):
        departamento = Departamento.objects.get(id=self.departamento.id)
        self.assertEqual(str(departamento), "Departamento de Álgebra")

    def test_profesor_str(self):
        profesor = Profesor.objects.get(id=self.profesor.id)
        expected_str = f"{profesor.documento_identidad}-{profesor.nombre}-{profesor.apellido}"
        self.assertEqual(str(profesor), expected_str)

    def test_documento_identidad_unique(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Profesor.objects.create(
                    nombre="OtroNombreCon50CaracteresExactamente" * 2,  # 50 characters
                    apellido="OtroApellido Largo",
                    documento_identidad="1234567890",  # Same document identity
                    correo_electronico="otroprofesor@universidad.com",
                    dependencia=self.dependencia,
                    departamento=self.departamento
                )

    def test_nombre_length_validation(self):
        with self.assertRaises(ValidationError):
            profesor = Profesor(
                nombre="NombreConMasDe50CaracteresLoQueDebeFallar",  # More than 50 characters
                apellido="Apellido Largos",
                documento_identidad="0987654321",
                correo_electronico="otroprofesor@universidad.com",
                dependencia=self.dependencia,
                departamento=self.departamento
            )
            profesor.clean()  # This should raise a ValidationError

    # EstrategiaCapacitacion model tests
    def test_estrategia_str(self):
        self.assertEqual(str(self.estrategia), "Estrategia A - 2024")

    def test_estado_choices(self):
        self.estrategia.estado = 'AP'
        self.estrategia.save()
        self.assertEqual(self.estrategia.estado, 'AP')

    def test_dependencia_digital_choices(self):
        self.estrategia.dependencia_digital = 'Gestión del conocimiento docente'
        self.estrategia.save()
        self.assertEqual(self.estrategia.dependencia_digital, 'Gestión del conocimiento docente')

    def test_periodo_choices(self):
        self.estrategia.periodo = 'II'
        self.estrategia.save()
        self.assertEqual(self.estrategia.periodo, 'II')

    def test_fecha_inicio_fecha_fin(self):
        self.assertEqual(self.estrategia.fecha_inicio, date(2024, 1, 1))
        self.assertEqual(self.estrategia.fecha_fin, date(2024, 1, 10))

    def test_duracion(self):
        self.assertEqual(self.estrategia.duracion, 10)

    def test_anio(self):
        self.assertEqual(self.estrategia.anio, 2024)
