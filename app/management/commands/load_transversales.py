from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Transversales, Nombreestrategia, Codigo, NivelRutaDocente

class Command(BaseCommand):
    help = 'Carga datos para el modelo Transversales desde un archivo Excel.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Ruta al archivo Excel con los datos.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            df = pd.read_excel(file_path)

            for index, row in df.iterrows():
                try:
                    # Buscar o crear Codigo por número exacto
                    codigo, _ = Codigo.objects.get_or_create(numero=row.get('codigo', ''))
                    if _:
                        self.stdout.write(self.style.SUCCESS(f'Creado Codigo: {codigo.numero}'))

                    # Buscar o crear Nombreestrategia por nombre exacto y con referencia a Codigo
                    nombre_estrategia_capacitacion, created = Nombreestrategia.objects.get_or_create(
                        nombre=row.get('nombre_estrategia_capacitacion', ''),
                        defaults={'codigo': codigo}
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Creado Nombreestrategia: {nombre_estrategia_capacitacion.nombre}'))

                    # Buscar o crear NivelRutaDocente por nombre exacto
                    nivel_ruta_docente, created = NivelRutaDocente.objects.get_or_create(nombre=row.get('nivel_ruta_docente', ''))
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Creado NivelRutaDocente: {nivel_ruta_docente.nombre}'))

                    # Convertir las fechas de Timestamp a datetime
                    try:
                        fecha_inicio = pd.to_datetime(row.get('fecha_inicio', ''), errors='coerce')
                        fecha_fin = pd.to_datetime(row.get('fecha_fin', ''), errors='coerce')
                        if pd.isna(fecha_inicio) or pd.isna(fecha_fin):
                            self.stdout.write(self.style.ERROR(f'Fechas inválidas en el índice {index}.'))
                            continue
                        fecha_inicio = fecha_inicio.date()
                        fecha_fin = fecha_fin.date()
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error en la conversión de fechas para el índice {index}: {str(e)}'))
                        continue

                    # Procesar y validar la duración
                    try:
                        duracion = float(str(row.get('duracion', '0')).replace(',', '.'))
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Error al convertir la duración a flotante en el índice {index}: {row.get("duracion", "0")}'))
                        continue

                    # Crear registro en Transversales
                    Transversales.objects.create(
                        nombre_estrategia_capacitacion=nombre_estrategia_capacitacion,
                        codigo=codigo,
                        nivel_ruta_docente=nivel_ruta_docente,
                        fecha_inicio=fecha_inicio,
                        fecha_fin=fecha_fin,
                        duracion=duracion,
                        anio=int(row.get('anio', 0))
                    )
                    self.stdout.write(self.style.SUCCESS(f'Datos cargados para Transversales con índice {index}'))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error en el índice {index}: {str(e)}'))

            self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente desde el archivo Excel.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocurrió un error al cargar los datos: {str(e)}'))
