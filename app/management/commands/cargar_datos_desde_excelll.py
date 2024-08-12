import pandas as pd
from django.core.management.base import BaseCommand
from app.models import RegistroHoras, Dinamización_de_conocimiento, Diseño_de_Ambientes, Gestión_información, Gestión_proyectos, Gestión_conocimiento, Producción_de_recursos, Transversales, Profesor

class Command(BaseCommand):
    help = 'Cargar datos desde un archivo Excel'

    def add_arguments(self, parser):
        parser.add_argument('ruta_archivo', type=str)

    def handle(self, *args, **kwargs):
        ruta_archivo = kwargs['ruta_archivo']
        self.cargar_datos_desde_excel(ruta_archivo)

    def cargar_datos_desde_excel(self, ruta_archivo):
        try:
            df = pd.read_excel(ruta_archivo)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"No se encontró el archivo en la ruta {ruta_archivo}"))
            return

        for _, fila in df.iterrows():
            profesor_documento = fila['documento_identidad']
            try:
                profesor = Profesor.objects.get(documento_identidad=profesor_documento)
            except Profesor.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"No se encontró el profesor con documento {profesor_documento}"))
                continue

            # Crear o actualizar RegistroHoras
            registro_horas, created = RegistroHoras.objects.update_or_create(
                profesor=profesor,
                defaults={}
            )

            # Asignar ManyToManyField usando .set()
            registro_horas.dinamizacion_de_redes_de_conocimiento.set(
                [int(x) for x in str(fila['dinamizacion_de_redes_de_conocimiento']).split(',') if x]
            )
            registro_horas.diseño_de_ambientes_virtuales_de_aprendizaje.set(
                [int(x) for x in str(fila['diseño_de_ambientes_virtuales_de_aprendizaje']).split(',') if x]
            )
            registro_horas.gestion_de_la_informacion.set(
                [int(x) for x in str(fila['gestion_de_la_informacion']).split(',') if x]
            )
            registro_horas.gestion_de_proyectos_con_TIC.set(
                [int(x) for x in str(fila['gestion_de_proyectos_con_TIC']).split(',') if x]
            )
            registro_horas.gestion_del_conocimiento_docente.set(
                [int(x) for x in str(fila['gestion_del_conocimiento_docente']).split(',') if x]
            )
            registro_horas.produccion_de_recursos_educativos_digitales.set(
                [int(x) for x in str(fila['produccion_de_recursos_educativos_digitales']).split(',') if x]
            )
            registro_horas.transversales.set(
                [int(x) for x in str(fila['transversales']).split(',') if x]
            )

            # Guardar los cambios
            registro_horas.save()

            self.stdout.write(self.style.SUCCESS(f"Registro creado/actualizado para profesor {profesor_documento}"))
