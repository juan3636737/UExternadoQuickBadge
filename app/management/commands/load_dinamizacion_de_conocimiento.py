from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Dinamización_de_conocimiento, Nombreestrategia, Codigo, NivelRutaDocente

class Command(BaseCommand):
    help = 'Carga datos para el modelo Dinamización_de_conocimiento desde un archivo Excel.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Ruta al archivo Excel con los datos.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            df = pd.read_excel(file_path)

            for index, row in df.iterrows():
                try:
                    # Obtener o crear Codigo
                    codigo, _ = Codigo.objects.get_or_create(
                        numero=row.get('codigo', '')
                    )

                    # Obtener o crear Nombreestrategia y asociar el Codigo
                    nombre_estrategia_capacitacion, created = Nombreestrategia.objects.get_or_create(
                        nombre=row.get('nombre_estrategia_capacitacion', ''),
                        defaults={'codigo': codigo}
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Creado Nombreestrategia: {nombre_estrategia_capacitacion.nombre}'))

                    # Obtener o crear NivelRutaDocente
                    nivel_ruta_docente, created = NivelRutaDocente.objects.get_or_create(
                        nombre=row.get('nivel_ruta_docente', '')
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Creado NivelRutaDocente: {nivel_ruta_docente.nombre}'))

                    # Convertir las fechas de Timestamp a datetime
                    fecha_inicio = pd.to_datetime(row.get('fecha_inicio', ''), errors='coerce')
                    fecha_fin = pd.to_datetime(row.get('fecha_fin', ''), errors='coerce')
                    if pd.isna(fecha_inicio) or pd.isna(fecha_fin):
                        self.stdout.write(self.style.ERROR(f'Error en la conversión de fechas para el índice {index}'))
                        continue

                    # Procesar el campo periodo
                    periodo = row.get('periodo', 'I')
                    if periodo not in ['I', 'II']:
                        periodo = 'I'  # Valor por defecto si no coincide con las opciones

                    # Procesar la duración y manejar comas como separadores decimales
                    duracion = row.get('duracion', 0)
                    if isinstance(duracion, str):
                        duracion = duracion.replace(',', '.')
                    try:
                        duracion = float(duracion)
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Error al convertir la duración a flotante en el índice {index}: {duracion}'))
                        continue

                    # Crear registro en Dinamización_de_conocimiento
                    Dinamización_de_conocimiento.objects.create(
                        nombre_estrategia_capacitacion=nombre_estrategia_capacitacion,
                        codigo=codigo,
                        nivel_ruta_docente=nivel_ruta_docente,
                        fecha_inicio=fecha_inicio.date(),
                        fecha_fin=fecha_fin.date(),
                        duracion=duracion,
                        periodo=periodo,
                        anio=int(row.get('anio', 0))
                    )
                    self.stdout.write(self.style.SUCCESS(f"Datos cargados para Dinamización_de_conocimiento con índice {index}"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error en el índice {index}: {e}'))

            self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente desde el archivo Excel.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocurrió un error al cargar los datos: {str(e)}'))
