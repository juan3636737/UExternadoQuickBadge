from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
import re

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "01 Facultades"


class Dependencia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "02 Dependencias"


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "03 Departamentos"


class NivelRutaDocente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "05 Niveles de Ruta Docente"


class Duracion(models.Model):
    duracion = models.DurationField()

    def __str__(self):
        # Convertir la duración a un string legible
        total_seconds = int(self.duracion.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}:{minutes:02}:{seconds:02}"


def validar_numero_puntos(value):
    # Validar que el valor contenga solo dígitos y puntos
    if not re.match(r'^[\d.]+$', value):
        raise ValidationError('El campo debe contener solo números y puntos.')

class Codigo(models.Model):
    numero = models.CharField(max_length=50, validators=[validar_numero_puntos], default='0')

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "06 Códigos"

class Nombreestrategia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.ForeignKey('Codigo', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo.numero if self.codigo else 'Sin código'})"

    class Meta:
        verbose_name_plural = "07 Estrategia capacitacion"

from django.core.exceptions import ValidationError
def validar_solo_letras(value):
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError('El campo solo puede contener letras y espacios.')
class Profesor(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_solo_letras])  
    apellido = models.CharField(max_length=100, validators=[validar_solo_letras])
    nombre_completo = models.CharField(max_length=200, editable=False)
    documento_identidad = models.CharField(max_length=20, unique=True)
    correo_electronico = models.EmailField(max_length=100, unique=True)  # Configurado correctamente
    correo_alternativo = models.CharField(max_length=100, blank=True)
    facultad = models.ManyToManyField(Facultad)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.nombre_completo = f"{self.nombre} {self.apellido}"
        super(Profesor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_completo} - {self.documento_identidad}"

    class Meta:
        verbose_name_plural = "04 Personas"


    
class Dinamización_de_conocimiento(models.Model):


    PERIODO_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
    ]
    nombre_estrategia_capacitacion = models.ForeignKey('Nombreestrategia', on_delete=models.CASCADE)
    codigo = models.ForeignKey('Codigo', on_delete=models.CASCADE, null=True, blank=True)
    nivel_ruta_docente = models.ForeignKey('NivelRutaDocente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.FloatField()  # Asegúrate de que este campo es un número representando la duración en horas
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES, default='I')
    anio = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Establecer el campo `codigo` basado en `nombre_estrategia_capacitacion`
        if self.nombre_estrategia_capacitacion:
            self.codigo = self.nombre_estrategia_capacitacion.codigo
        
        super().save(*args, **kwargs)
        
    def truncate_nombre(self, nombre, max_length):
        """Truncate the name based on the max_length provided."""
        if len(nombre) > max_length:
            return nombre[:max_length] + '...'
        return nombre

    def get_truncated_nombre(self, initial_length, final_length):
        """Return the truncated nombre based on the provided initial_length and final_length."""
        nombre = self.nombre_estrategia_capacitacion.nombre
        truncated_nombre = self.truncate_nombre(nombre, initial_length)
        final_truncated_nombre = self.truncate_nombre(truncated_nombre, final_length)
        return final_truncated_nombre

    def __str__(self, initial_length=300, final_length=100):
        """Return the string representation of the model with configurable truncation lengths."""
        nombre_truncated = self.get_truncated_nombre(initial_length, final_length)
        return f"{nombre_truncated} - {self.fecha_inicio}"

    class Meta:
        verbose_name_plural = "08 Dinamización de redes de conocimiento"

class Diseño_de_Ambientes(models.Model):


    PERIODO_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
    ]
    nombre_estrategia_capacitacion = models.ForeignKey('Nombreestrategia', on_delete=models.CASCADE)
    codigo = models.ForeignKey('Codigo', on_delete=models.CASCADE)
    nivel_ruta_docente = models.ForeignKey('NivelRutaDocente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.FloatField()  # Asegúrate de que este campo es un número representando la duración en horas
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES, default='I')
    anio = models.PositiveIntegerField()

    def truncate_nombre(self, nombre, max_length):
        """Truncate the name based on the max_length provided."""
        if len(nombre) > max_length:
            return nombre[:max_length] + '...'
        return nombre

    def get_truncated_nombre(self, initial_length, final_length):
        """Return the truncated nombre based on the provided initial_length and final_length."""
        nombre = self.nombre_estrategia_capacitacion.nombre
        truncated_nombre = self.truncate_nombre(nombre, initial_length)
        final_truncated_nombre = self.truncate_nombre(truncated_nombre, final_length)
        return final_truncated_nombre

    def __str__(self, initial_length=300, final_length=100):
        """Return the string representation of the model with configurable truncation lengths."""
        nombre_truncated = self.get_truncated_nombre(initial_length, final_length)
        return f"{nombre_truncated} - {self.fecha_inicio}"

    class Meta:
        verbose_name_plural = "09 Diseño de Ambientes Virtuales de aprendizaje"

class Gestión_información(models.Model):


    PERIODO_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
    ]
    nombre_estrategia_capacitacion = models.ForeignKey('Nombreestrategia', on_delete=models.CASCADE)
    codigo = models.ForeignKey('Codigo', on_delete=models.CASCADE)
    nivel_ruta_docente = models.ForeignKey('NivelRutaDocente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.FloatField()  # Asegúrate de que este campo es un número representando la duración en horas
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES, default='I')
    anio = models.PositiveIntegerField()

    def truncate_nombre(self, nombre, max_length):
        """Truncate the name based on the max_length provided."""
        if len(nombre) > max_length:
            return nombre[:max_length] + '...'
        return nombre

    def get_truncated_nombre(self, initial_length, final_length):
        """Return the truncated nombre based on the provided initial_length and final_length."""
        nombre = self.nombre_estrategia_capacitacion.nombre
        truncated_nombre = self.truncate_nombre(nombre, initial_length)
        final_truncated_nombre = self.truncate_nombre(truncated_nombre, final_length)
        return final_truncated_nombre

    def __str__(self, initial_length=300, final_length=100):
        """Return the string representation of the model with configurable truncation lengths."""
        nombre_truncated = self.get_truncated_nombre(initial_length, final_length)
        return f"{nombre_truncated} - {self.fecha_inicio}"

    class Meta:
        verbose_name_plural = "10 Gestión de la información"
    
class Gestión_proyectos(models.Model):

    PERIODO_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
    ]
    nombre_estrategia_capacitacion = models.ForeignKey('Nombreestrategia', on_delete=models.CASCADE)
    codigo = models.ForeignKey('Codigo', on_delete=models.CASCADE)
    nivel_ruta_docente = models.ForeignKey('NivelRutaDocente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.FloatField()  # Asegúrate de que este campo es un número representando la duración en horas
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES, default='I')
    anio = models.PositiveIntegerField()

    def truncate_nombre(self, nombre, max_length):
        """Truncate the name based on the max_length provided."""
        if len(nombre) > max_length:
            return nombre[:max_length] + '...'
        return nombre

    def get_truncated_nombre(self, initial_length, final_length):
        """Return the truncated nombre based on the provided initial_length and final_length."""
        nombre = self.nombre_estrategia_capacitacion.nombre
        truncated_nombre = self.truncate_nombre(nombre, initial_length)
        final_truncated_nombre = self.truncate_nombre(truncated_nombre, final_length)
        return final_truncated_nombre

    def __str__(self, initial_length=300, final_length=100):
        """Return the string representation of the model with configurable truncation lengths."""
        nombre_truncated = self.get_truncated_nombre(initial_length, final_length)
        return f"{nombre_truncated} - {self.fecha_inicio}"

    class Meta:
        verbose_name_plural = "11 Gestión de proyectos con TIC"
    
class Gestión_conocimiento(models.Model):

    PERIODO_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
    ]
    nombre_estrategia_capacitacion = models.ForeignKey('Nombreestrategia', on_delete=models.CASCADE)
    codigo = models.ForeignKey('Codigo', on_delete=models.CASCADE)
    nivel_ruta_docente = models.ForeignKey('NivelRutaDocente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.FloatField()  # Asegúrate de que este campo es un número representando la duración en horas
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES, default='I')
    anio = models.PositiveIntegerField()

    def truncate_nombre(self, nombre, max_length):
        """Truncate the name based on the max_length provided."""
        if len(nombre) > max_length:
            return nombre[:max_length] + '...'
        return nombre

    def get_truncated_nombre(self, initial_length, final_length):
        """Return the truncated nombre based on the provided initial_length and final_length."""
        nombre = self.nombre_estrategia_capacitacion.nombre
        truncated_nombre = self.truncate_nombre(nombre, initial_length)
        final_truncated_nombre = self.truncate_nombre(truncated_nombre, final_length)
        return final_truncated_nombre

    def __str__(self, initial_length=300, final_length=100):
        """Return the string representation of the model with configurable truncation lengths."""
        nombre_truncated = self.get_truncated_nombre(initial_length, final_length)
        return f"{nombre_truncated} - {self.fecha_inicio}"

    class Meta:
        verbose_name_plural = "12 Gestión del conocimiento docente"   
class Transversales(models.Model):

    PERIODO_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
    ]
    nombre_estrategia_capacitacion = models.ForeignKey('Nombreestrategia', on_delete=models.CASCADE)
    codigo = models.ForeignKey('Codigo', on_delete=models.CASCADE)
    nivel_ruta_docente = models.ForeignKey('NivelRutaDocente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.FloatField()  # Asegúrate de que este campo es un número representando la duración en horas
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES, default='I')
    anio = models.PositiveIntegerField()

    def truncate_nombre(self, nombre, max_length):
        """Truncate the name based on the max_length provided."""
        if len(nombre) > max_length:
            return nombre[:max_length] + '...'
        return nombre

    def get_truncated_nombre(self, initial_length, final_length):
        """Return the truncated nombre based on the provided initial_length and final_length."""
        nombre = self.nombre_estrategia_capacitacion.nombre
        truncated_nombre = self.truncate_nombre(nombre, initial_length)
        final_truncated_nombre = self.truncate_nombre(truncated_nombre, final_length)
        return final_truncated_nombre

    def __str__(self, initial_length=300, final_length=100):
        """Return the string representation of the model with configurable truncation lengths."""
        nombre_truncated = self.get_truncated_nombre(initial_length, final_length)
        return f"{nombre_truncated} - {self.fecha_inicio}"

    class Meta:
        verbose_name_plural = "13 Transversales"
class Producción_de_recursos(models.Model):

    PERIODO_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
    ]
    nombre_estrategia_capacitacion = models.ForeignKey('Nombreestrategia', on_delete=models.CASCADE)
    codigo = models.ForeignKey('Codigo', on_delete=models.CASCADE)
    nivel_ruta_docente = models.ForeignKey('NivelRutaDocente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    duracion = models.FloatField()  # Asegúrate de que este campo es un número representando la duración en horas
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES, default='I')
    anio = models.PositiveIntegerField()

    def truncate_nombre(self, nombre, max_length):
        """Truncate the name based on the max_length provided."""
        if len(nombre) > max_length:
            return nombre[:max_length] + '...'
        return nombre

    def get_truncated_nombre(self, initial_length, final_length):
        """Return the truncated nombre based on the provided initial_length and final_length."""
        nombre = self.nombre_estrategia_capacitacion.nombre
        truncated_nombre = self.truncate_nombre(nombre, initial_length)
        final_truncated_nombre = self.truncate_nombre(truncated_nombre, final_length)
        return final_truncated_nombre

    def __str__(self, initial_length=300, final_length=100):
        """Return the string representation of the model with configurable truncation lengths."""
        nombre_truncated = self.get_truncated_nombre(initial_length, final_length)
        return f"{nombre_truncated} - {self.fecha_inicio}"

    class Meta:
        verbose_name_plural = "14 Producción de recursos educativos digitales" 
        


class RegistroHoras(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, unique=True)
    
    # Competencias desde el panel le selecciono las estrategias de capacitacion que deseo
    dinamizacion_de_redes_de_conocimiento = models.ManyToManyField(Dinamización_de_conocimiento, related_name='dinamizacion_redes', blank=True)
    diseño_de_ambientes_virtuales_de_aprendizaje = models.ManyToManyField(Diseño_de_Ambientes, related_name='diseno_ambientes', blank=True)
    gestion_de_la_informacion = models.ManyToManyField(Gestión_información, related_name='gestion_informacion', blank=True)
    gestion_de_proyectos_con_TIC = models.ManyToManyField(Gestión_proyectos, related_name='gestion_proyectos', blank=True)
    gestion_del_conocimiento_docente = models.ManyToManyField(Gestión_conocimiento, related_name='gestion_conocimiento', blank=True)
    produccion_de_recursos_educativos_digitales = models.ManyToManyField(Producción_de_recursos, related_name='produccion_recursos', blank=True)
    transversales = models.ManyToManyField(Transversales, related_name='transversales', blank=True)


    # Nuevos acumuladores por codigo este aun no tiene acomulador tu lo tienes que hacer independiente a los otros este tiene una condicion 
    # la cual es que el suma las estrategias de capacitacion si y solo si sus codigos son dijerentes si agrego dos estartegias de capacitacion con el mismo 
    # codigo solo debe coger un valor de duracion y sumarlo con otro valor de duracion de otra estrategia de capatciatcion con codigo diferente 
    horas_dinamizacion_redes_insignia = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_diseno_ambientes_insignia = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_gestion_informacion_insignia = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_gestion_proyectos_insignia = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_gestion_conocimiento_insignia = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_produccion_recursos_insignia = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_transversales_insignia = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    

    # Campos para almacenar los niveles
    nivel_dinamizacion_redes = models.CharField(max_length=30, blank=True)
    nivel_diseno_ambientes = models.CharField(max_length=30, blank=True)
    nivel_gestion_informacion = models.CharField(max_length=30, blank=True)
    nivel_gestion_proyectos = models.CharField(max_length=30, blank=True)
    nivel_gestion_conocimiento = models.CharField(max_length=30, blank=True)
    nivel_produccion_recursos = models.CharField(max_length=30, blank=True)
    nivel_transversales = models.CharField(max_length=30, blank=True)


    # Acumuladores de horas totales se acomulan por cada competencia ingresa ya tiene su acomulador en signals no quiero que lo edites 
    acomulador_dinamizacion_redes = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    acomulador_diseno_ambientes = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    acomulador_gestion_informacion = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    acomulador_gestion_proyectos = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    acomulador_gestion_conocimiento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    acomulador_produccion_recursos = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    acomulador_transversales = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_trabajadas = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    fecha_registro = models.DateField(auto_now_add=True)
    nivel = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = "15 Insignia de nivel"

    
    # Métodos para obtener el nivel de cada campo
    def get_nivel_dinamizacion_redes(self):
        if self.horas_dinamizacion_redes_insignia >= 50:
            return 'Avanzado o Innovador'
        elif self.horas_dinamizacion_redes_insignia >= 40:
            return 'Intermedio o Integrador'
        elif self.horas_dinamizacion_redes_insignia >= 20:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'

    def get_nivel_diseno_ambientes(self):
        if self.horas_diseno_ambientes_insignia >= 100:
            return 'Avanzado o Innovador'
        elif self.horas_diseno_ambientes_insignia >= 90:
            return 'Intermedio o Integrador'
        elif self.horas_diseno_ambientes_insignia >= 45:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'

    def get_nivel_gestion_informacion(self):
        if self.horas_gestion_informacion_insignia >= 50:
            return 'Avanzado o Innovador'
        elif self.horas_gestion_informacion_insignia >= 40:
            return 'Intermedio o Integrador'
        elif self.horas_gestion_informacion_insignia >= 20:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'

    def get_nivel_gestion_proyectos(self):
        if self.horas_gestion_proyectos_insignia >= 350:
            return 'Avanzado o Innovador'
        elif self.horas_gestion_proyectos_insignia >= 240:
            return 'Intermedio o Integrador'
        elif self.horas_gestion_proyectos_insignia >= 120:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'

    def get_nivel_gestion_conocimiento(self):
        if self.horas_gestion_conocimiento_insignia >= 60:
            return 'Avanzado o Innovador'
        elif self.horas_gestion_conocimiento_insignia >= 40:
            return 'Intermedio o Integrador'
        elif self.horas_gestion_conocimiento_insignia >= 20:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'

    def get_nivel_produccion_recursos(self):
        if self.horas_produccion_recursos_insignia >= 80:
            return 'Avanzado o Innovador'
        elif self.horas_produccion_recursos_insignia >= 70:
            return 'Intermedio o Integrador'
        elif self.horas_produccion_recursos_insignia >= 35:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'

    def get_nivel_transversales(self):
        if self.horas_transversales_insignia >= 350:
            return 'Avanzado o Innovador'
        elif self.horas_transversales_insignia >= 240:
            return 'Intermedio o Integrador'
        elif self.horas_transversales_insignia >= 120:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'

    def get_nivel(self):
        if self.horas_trabajadas >= 360:
            return 'Avanzado o Innovador'
        elif self.horas_trabajadas >= 240:
            return 'Intermedio o Integrador'
        elif self.horas_trabajadas >= 120:
            return 'Inicial o Explorador'
        else:
            return 'No clasificado'
    
    def save(self, *args, **kwargs):
        # Actualizar los niveles antes de guardar
        self.nivel_dinamizacion_redes = self.get_nivel_dinamizacion_redes()
        self.nivel_diseno_ambientes = self.get_nivel_diseno_ambientes()
        self.nivel_gestion_informacion = self.get_nivel_gestion_informacion()
        self.nivel_gestion_proyectos = self.get_nivel_gestion_proyectos()
        self.nivel_gestion_conocimiento = self.get_nivel_gestion_conocimiento()
        self.nivel_produccion_recursos = self.get_nivel_produccion_recursos()
        self.nivel_transversales = self.get_nivel_transversales()
        self.nivel = self.get_nivel()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.profesor} - {self.horas_trabajadas} horas - Nivel: {self.get_nivel()}"



class Carrusel(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='carrusel/')

    class Meta:
        verbose_name_plural = "16 Carrusel Eventos"

class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    correo = models.EmailField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='personal/')

    def _str_(self):
        return f"{self.nombre} - {self.cargo}"

    class Meta:
        verbose_name_plural = "17 Carrusel Personal"

class ProfesorDestacado(models.Model):
    registro_horas = models.ForeignKey(RegistroHoras, on_delete=models.CASCADE, related_name='profesores_destacados', unique=True)
    imagen = models.ImageField(upload_to='profesores_destacados')  # Campo para subir imágenes

    def _str_(self):
        return f"{self.registro_horas.profesor.nombre} - {self.registro_horas.fecha_registro}"
    class Meta:
        verbose_name_plural = "18 Personas destacadas"