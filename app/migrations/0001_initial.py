# Generated by Django 4.2.6 on 2024-08-09 20:35

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(upload_to='carrusel/')),
            ],
            options={
                'verbose_name_plural': '16 Carrusel Eventos',
            },
        ),
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(default='0', max_length=50, validators=[app.models.validar_numero_puntos])),
            ],
            options={
                'verbose_name_plural': '06 Códigos',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '03 Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '02 Dependencias',
            },
        ),
        migrations.CreateModel(
            name='Dinamización_de_conocimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.FloatField()),
                ('periodo', models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=2)),
                ('anio', models.PositiveIntegerField()),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.codigo')),
            ],
            options={
                'verbose_name_plural': '08 Dinamización de redes de conocimiento',
            },
        ),
        migrations.CreateModel(
            name='Diseño_de_Ambientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.FloatField()),
                ('periodo', models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=2)),
                ('anio', models.PositiveIntegerField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.codigo')),
            ],
            options={
                'verbose_name_plural': '09 Diseño de Ambientes Virtuales de aprendizaje',
            },
        ),
        migrations.CreateModel(
            name='Duracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '01 Facultades',
            },
        ),
        migrations.CreateModel(
            name='Gestión_conocimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.FloatField()),
                ('periodo', models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=2)),
                ('anio', models.PositiveIntegerField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.codigo')),
            ],
            options={
                'verbose_name_plural': '12 Gestión del conocimiento docente',
            },
        ),
        migrations.CreateModel(
            name='Gestión_información',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.FloatField()),
                ('periodo', models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=2)),
                ('anio', models.PositiveIntegerField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.codigo')),
            ],
            options={
                'verbose_name_plural': '10 Gestión de la información',
            },
        ),
        migrations.CreateModel(
            name='Gestión_proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.FloatField()),
                ('periodo', models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=2)),
                ('anio', models.PositiveIntegerField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.codigo')),
            ],
            options={
                'verbose_name_plural': '11 Gestión de proyectos con TIC',
            },
        ),
        migrations.CreateModel(
            name='NivelRutaDocente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '05 Niveles de Ruta Docente',
            },
        ),
        migrations.CreateModel(
            name='Nombreestrategia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.codigo')),
            ],
            options={
                'verbose_name_plural': '07 Estrategia capacitacion',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(upload_to='personal/')),
            ],
            options={
                'verbose_name_plural': '17 Carrusel Personal',
            },
        ),
        migrations.CreateModel(
            name='Producción_de_recursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.FloatField()),
                ('periodo', models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=2)),
                ('anio', models.PositiveIntegerField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.codigo')),
                ('nivel_ruta_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivelrutadocente')),
                ('nombre_estrategia_capacitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nombreestrategia')),
            ],
            options={
                'verbose_name_plural': '14 Producción de recursos educativos digitales',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[app.models.validar_solo_letras])),
                ('apellido', models.CharField(max_length=100, validators=[app.models.validar_solo_letras])),
                ('nombre_completo', models.CharField(editable=False, max_length=200)),
                ('documento_identidad', models.CharField(max_length=20, unique=True)),
                ('correo_electronico', models.EmailField(max_length=100, unique=True)),
                ('correo_alternativo', models.CharField(blank=True, max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departamento')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dependencia')),
                ('facultad', models.ManyToManyField(to='app.facultad')),
            ],
            options={
                'verbose_name_plural': '04 Personas',
            },
        ),
        migrations.CreateModel(
            name='Transversales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.FloatField()),
                ('periodo', models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=2)),
                ('anio', models.PositiveIntegerField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.codigo')),
                ('nivel_ruta_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivelrutadocente')),
                ('nombre_estrategia_capacitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nombreestrategia')),
            ],
            options={
                'verbose_name_plural': '13 Transversales',
            },
        ),
        migrations.CreateModel(
            name='RegistroHoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas_dinamizacion_redes_insignia', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('horas_diseno_ambientes_insignia', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('horas_gestion_informacion_insignia', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('horas_gestion_proyectos_insignia', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('horas_gestion_conocimiento_insignia', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('horas_produccion_recursos_insignia', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('horas_transversales_insignia', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('nivel_dinamizacion_redes', models.CharField(blank=True, max_length=30)),
                ('nivel_diseno_ambientes', models.CharField(blank=True, max_length=30)),
                ('nivel_gestion_informacion', models.CharField(blank=True, max_length=30)),
                ('nivel_gestion_proyectos', models.CharField(blank=True, max_length=30)),
                ('nivel_gestion_conocimiento', models.CharField(blank=True, max_length=30)),
                ('nivel_produccion_recursos', models.CharField(blank=True, max_length=30)),
                ('nivel_transversales', models.CharField(blank=True, max_length=30)),
                ('acomulador_dinamizacion_redes', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acomulador_diseno_ambientes', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acomulador_gestion_informacion', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acomulador_gestion_proyectos', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acomulador_gestion_conocimiento', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acomulador_produccion_recursos', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acomulador_transversales', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('horas_trabajadas', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('nivel', models.CharField(blank=True, max_length=30)),
                ('dinamizacion_de_redes_de_conocimiento', models.ManyToManyField(blank=True, related_name='dinamizacion_redes', to='app.dinamización_de_conocimiento')),
                ('diseño_de_ambientes_virtuales_de_aprendizaje', models.ManyToManyField(blank=True, related_name='diseno_ambientes', to='app.diseño_de_ambientes')),
                ('gestion_de_la_informacion', models.ManyToManyField(blank=True, related_name='gestion_informacion', to='app.gestión_información')),
                ('gestion_de_proyectos_con_TIC', models.ManyToManyField(blank=True, related_name='gestion_proyectos', to='app.gestión_proyectos')),
                ('gestion_del_conocimiento_docente', models.ManyToManyField(blank=True, related_name='gestion_conocimiento', to='app.gestión_conocimiento')),
                ('produccion_de_recursos_educativos_digitales', models.ManyToManyField(blank=True, related_name='produccion_recursos', to='app.producción_de_recursos')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profesor', unique=True)),
                ('transversales', models.ManyToManyField(blank=True, related_name='transversales', to='app.transversales')),
            ],
            options={
                'verbose_name_plural': '15 Insignia de nivel',
            },
        ),
        migrations.CreateModel(
            name='ProfesorDestacado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='profesores_destacados')),
                ('registro_horas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesores_destacados', to='app.registrohoras', unique=True)),
            ],
            options={
                'verbose_name_plural': '18 Personas destacadas',
            },
        ),
        migrations.AddField(
            model_name='gestión_proyectos',
            name='nivel_ruta_docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivelrutadocente'),
        ),
        migrations.AddField(
            model_name='gestión_proyectos',
            name='nombre_estrategia_capacitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nombreestrategia'),
        ),
        migrations.AddField(
            model_name='gestión_información',
            name='nivel_ruta_docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivelrutadocente'),
        ),
        migrations.AddField(
            model_name='gestión_información',
            name='nombre_estrategia_capacitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nombreestrategia'),
        ),
        migrations.AddField(
            model_name='gestión_conocimiento',
            name='nivel_ruta_docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivelrutadocente'),
        ),
        migrations.AddField(
            model_name='gestión_conocimiento',
            name='nombre_estrategia_capacitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nombreestrategia'),
        ),
        migrations.AddField(
            model_name='diseño_de_ambientes',
            name='nivel_ruta_docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivelrutadocente'),
        ),
        migrations.AddField(
            model_name='diseño_de_ambientes',
            name='nombre_estrategia_capacitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nombreestrategia'),
        ),
        migrations.AddField(
            model_name='dinamización_de_conocimiento',
            name='nivel_ruta_docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivelrutadocente'),
        ),
        migrations.AddField(
            model_name='dinamización_de_conocimiento',
            name='nombre_estrategia_capacitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nombreestrategia'),
        ),
    ]
