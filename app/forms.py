from django import forms
from .models import RegistroHoras, Profesor

class ProfesorModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre_completo

class RegistroHorasForm(forms.ModelForm):
    profesor = ProfesorModelChoiceField(
        queryset=Profesor.objects.all(),
        label='Profesor',
        widget=forms.Select
    )

    class Meta:
        model = RegistroHoras
        fields = '__all__'