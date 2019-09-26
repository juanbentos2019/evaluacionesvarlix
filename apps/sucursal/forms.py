from django import forms
from .models import local, empleado, evalua, tarjeta


class localForm(forms.ModelForm):
	class Meta:
		model = local
		fields = ['denominacion', 'encargado']


class empleadoForm(forms.ModelForm):
	class Meta:
		model = empleado
		fields = ['nombre','cedula','antiguedad','local_id']

class evaluaForm(forms.ModelForm):
	class Meta:
		model = evalua
		fields = ['asistencia','puntualidad','presencia','cliente','equipo','compromiso','iniciativa','id_evaluando']


class tarjetaForm(forms.ModelForm):
	class Meta:
		model = tarjeta
		fields = ['p_nombre','s_nombre','p_apellido','s_apellido','lugar']