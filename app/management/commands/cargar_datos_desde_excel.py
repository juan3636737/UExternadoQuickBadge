import pandas as pd
from django.core.management.base import BaseCommand
from app.models import Profesor, Facultad, Dependencia, Departamento
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Carga datos de personas desde un archivo Excel a la base de datos'

    def add_arguments(self, parser):
        parser.add_argument('ruta_archivo', type=str, help='Ruta del archivo Excel')

    def handle(self, *args, **kwargs):
        ruta_archivo = kwargs['ruta_archivo']
        datos = pd.read_excel(ruta_archivo)

        errores = []
        for _, row in datos.iterrows():
            facultad_nombres = row['facultad'].split(',')  # Suponiendo que los nombres de facultad están separados por comas
            facultades = []
            for nombre in facultad_nombres:
                facultad, _ = Facultad.objects.get_or_create(nombre=nombre.strip())
                facultades.append(facultad)

            dependencia, _ = Dependencia.objects.get_or_create(nombre=row['dependencia'])
            departamento, _ = Departamento.objects.get_or_create(nombre=row['departamento'])

            try:
                profesor, created = Profesor.objects.update_or_create(
                    documento_identidad=row['documento_identidad'],
                    defaults={
                        'nombre': row['nombre'],
                        'apellido': row['apellido'],
                        'correo_electronico': row['correo_electronico'],
                        'correo_alternativo': row.get('correo_alternativo', ''),
                        'dependencia': dependencia,
                        'departamento': departamento,
                    }
                )
                # Actualizar las relaciones ManyToMany después de crear el objeto
                profesor.facultad.set(facultades)
            except IntegrityError as e:
                errores.append(f'Error con el correo {row["correo_electronico"]}: {e}')
                continue

        if errores:
            self.stdout.write(self.style.ERROR('Se encontraron los siguientes errores:'))
            for error in errores:
                self.stdout.write(self.style.ERROR(error))
        else:
            self.stdout.write(self.style.SUCCESS('Datos de personas cargados exitosamente'))
