from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db import models
from .models import RegistroHoras

@receiver(m2m_changed, sender=RegistroHoras.dinamizacion_de_redes_de_conocimiento.through)
@receiver(m2m_changed, sender=RegistroHoras.diseño_de_ambientes_virtuales_de_aprendizaje.through)
@receiver(m2m_changed, sender=RegistroHoras.gestion_de_la_informacion.through)
@receiver(m2m_changed, sender=RegistroHoras.gestion_de_proyectos_con_TIC.through)
@receiver(m2m_changed, sender=RegistroHoras.gestion_del_conocimiento_docente.through)
@receiver(m2m_changed, sender=RegistroHoras.produccion_de_recursos_educativos_digitales.through)
@receiver(m2m_changed, sender=RegistroHoras.transversales.through)
def update_horas_trabajadas(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = 0
        related_fields = [
            instance.dinamizacion_de_redes_de_conocimiento,
            instance.diseño_de_ambientes_virtuales_de_aprendizaje,
            instance.gestion_de_la_informacion,
            instance.gestion_de_proyectos_con_TIC,
            instance.gestion_del_conocimiento_docente,
            instance.produccion_de_recursos_educativos_digitales,
            instance.transversales,
        ]
        
        for field in related_fields:
            total_horas += field.aggregate(total=models.Sum('duracion'))['total'] or 0
        
        instance.horas_trabajadas = total_horas
        instance.save()



@receiver(m2m_changed, sender=RegistroHoras.dinamizacion_de_redes_de_conocimiento.through)
def update_horas_dinamizacion_redes(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = instance.dinamizacion_de_redes_de_conocimiento.aggregate(total=models.Sum('duracion'))['total'] or 0
        instance.acomulador_dinamizacion_redes = total_horas
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.diseño_de_ambientes_virtuales_de_aprendizaje.through)
def update_horas_diseno_ambientes(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = instance.diseño_de_ambientes_virtuales_de_aprendizaje.aggregate(total=models.Sum('duracion'))['total'] or 0
        instance.acomulador_diseno_ambientes = total_horas
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.gestion_de_la_informacion.through)
def update_horas_gestion_informacion(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = instance.gestion_de_la_informacion.aggregate(total=models.Sum('duracion'))['total'] or 0
        instance.acomulador_gestion_informacion = total_horas
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.gestion_de_proyectos_con_TIC.through)
def update_horas_gestion_proyectos(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = instance.gestion_de_proyectos_con_TIC.aggregate(total=models.Sum('duracion'))['total'] or 0
        instance.acomulador_gestion_proyectos = total_horas
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.gestion_del_conocimiento_docente.through)
def update_horas_gestion_conocimiento(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = instance.gestion_del_conocimiento_docente.aggregate(total=models.Sum('duracion'))['total'] or 0
        instance.acomulador_gestion_conocimiento = total_horas
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.produccion_de_recursos_educativos_digitales.through)
def update_horas_produccion_recursos(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = instance.produccion_de_recursos_educativos_digitales.aggregate(total=models.Sum('duracion'))['total'] or 0
        instance.acomulador_produccion_recursos = total_horas
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.transversales.through)
def update_horas_transversales(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas = instance.transversales.aggregate(total=models.Sum('duracion'))['total'] or 0
        instance.acomulador_transversales = total_horas
        instance.save()
        
        


def calculate_unique_code_hours(strategy_queryset):
    """Calculate total hours considering only one duration per unique code."""
    # Get all distinct codes
    codes = strategy_queryset.values_list('codigo', flat=True).distinct()
    
    total_duration = 0
    for code in codes:
        # Get the maximum duration for each unique code
        max_duration = strategy_queryset.filter(codigo=code).aggregate(max_duration=models.Max('duracion'))['max_duration']
        if max_duration:
            total_duration += max_duration
    
    return total_duration

@receiver(m2m_changed, sender=RegistroHoras.dinamizacion_de_redes_de_conocimiento.through)
def update_horas_dinamizacion_redes_codigo(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas_codigo = calculate_unique_code_hours(instance.dinamizacion_de_redes_de_conocimiento)
        instance.horas_dinamizacion_redes_insignia = total_horas_codigo
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.diseño_de_ambientes_virtuales_de_aprendizaje.through)
def update_horas_diseno_ambientes_codigo(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas_codigo = calculate_unique_code_hours(instance.diseño_de_ambientes_virtuales_de_aprendizaje)
        instance.horas_diseno_ambientes_insignia = total_horas_codigo
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.gestion_de_la_informacion.through)
def update_horas_gestion_informacion_codigo(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas_codigo = calculate_unique_code_hours(instance.gestion_de_la_informacion)
        instance.horas_gestion_informacion_insignia = total_horas_codigo
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.gestion_de_proyectos_con_TIC.through)
def update_horas_gestion_proyectos_codigo(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas_codigo = calculate_unique_code_hours(instance.gestion_de_proyectos_con_TIC)
        instance.horas_gestion_proyectos_insignia = total_horas_codigo
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.gestion_del_conocimiento_docente.through)
def update_horas_gestion_conocimiento_codigo(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas_codigo = calculate_unique_code_hours(instance.gestion_del_conocimiento_docente)
        instance.horas_gestion_conocimiento_insignia = total_horas_codigo
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.produccion_de_recursos_educativos_digitales.through)
def update_horas_produccion_recursos_codigo(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas_codigo = calculate_unique_code_hours(instance.produccion_de_recursos_educativos_digitales)
        instance.horas_produccion_recursos_insignia = total_horas_codigo
        instance.save()

@receiver(m2m_changed, sender=RegistroHoras.transversales.through)
def update_horas_transversales_codigo(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        total_horas_codigo = calculate_unique_code_hours(instance.transversales)
        instance.horas_transversales_insignia = total_horas_codigo
        instance.save()