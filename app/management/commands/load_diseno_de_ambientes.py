from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Diseño_de_Ambientes, Nombreestrategia, Codigo, NivelRutaDocente

class Command(BaseCommand):
    help = 'Carga datos para el modelo Diseño_de_Ambientes desde un archivo Excel.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Ruta al archivo Excel con los datos.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            df = pd.read_excel(file_path)

            for index, row in df.iterrows():
                try:
                    # Buscar o crear Codigo
                    codigo, _ = Codigo.objects.get_or_create(
                        numero=row.get('codigo', '')
                    )

                    # Buscar o crear Nombreestrategia y asociar el Codigo
                    nombre_estrategia, created = Nombreestrategia.objects.get_or_create(
                        nombre=row.get('nombre_estrategia_capacitacion', ''),
                        defaults={'codigo': codigo}
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Creado Nombreestrategia: {nombre_estrategia.nombre}'))

                    # Buscar o crear NivelRutaDocente por nombre exacto
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

                    fecha_inicio = fecha_inicio.date()
                    fecha_fin = fecha_fin.date()

                    # Reemplazar comas por puntos en la duración
                    duracion_str = str(row.get('duracion', '0')).replace(',', '.')
                    self.stdout.write(self.style.INFO(f'Valor de duración antes de la conversión: {duracion_str}'))
                    try:
                        duracion = float(duracion_str)
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Error al convertir la duración a flotante en el índice {index}: {duracion_str}'))
                        continue

                    # Crear registro en Diseño_de_Ambientes
                    try:
                        Diseño_de_Ambientes.objects.create(
                            nombre_estrategia_capacitacion=nombre_estrategia,
                            codigo=codigo,
                            nivel_ruta_docente=nivel_ruta_docente,
                            fecha_inicio=fecha_inicio,
                            fecha_fin=fecha_fin,
                            duracion=duracion,
                            anio=int(row.get('anio', 0))
                        )
                        self.stdout.write(self.style.SUCCESS(f'Datos cargados para Diseño_de_Ambientes con índice {index}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error al crear Diseño_de_Ambientes en el índice {index}: {str(e)}'))
                        continue

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error en el índice {index}: {str(e)}'))

            self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente desde el archivo Excel.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocurrió un error al cargar los datos: {str(e)}'))
