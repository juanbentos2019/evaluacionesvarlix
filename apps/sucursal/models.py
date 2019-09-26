from django.db import models





class local(models.Model):
	id = models.AutoField(primary_key=True)
	denominacion = models.CharField(max_length=200, unique=True)
	encargado = models.CharField(max_length=200)

	class Meta:
		verbose_name='local'
		verbose_name_plural='locales'
		ordering=['denominacion']

	def __str__(self):
		return self.denominacion

class empleado(models.Model):
	id = models.AutoField(primary_key=True)
	cedula = models.IntegerField(verbose_name='Cedula de Identidad')
	nombre = models.CharField(max_length=200,blank=False, null=False)
	antiguedad = models.IntegerField(verbose_name='Antigüedad')
	#asistencia = models.IntegerField(verbose_name='Asistencia')
	#puntualidad = models.IntegerField(verbose_name='Puntualidad')
	#presencia = models.IntegerField(verbose_name='Buena Presencia')
	#cliente = models.IntegerField(verbose_name='Orientaion/Atencion al Cliente')
	#equipo = models.IntegerField(verbose_name='Trabajo en Equipo')
	#compromiso = models.IntegerField(verbose_name='Compromiso')
	#iniciativa = models.IntegerField(verbose_name='Iniciativa')
	local_id = models.ForeignKey(local, on_delete=models.CASCADE)

	class Meta:
		verbose_name='Empleado'
		verbose_name_plural='Empleados'
		ordering=['nombre']

	def __str__(self):
		return self.nombre

class evalua(models.Model):
	id = models.AutoField(primary_key=True)
	asistencia = models.IntegerField(null=True,verbose_name='Asistencia')
	puntualidad = models.IntegerField(null=True,verbose_name='Puntualidad')
	presencia = models.IntegerField(null=True,verbose_name='Buena Presencia')
	cliente = models.IntegerField(null=True,verbose_name='Orientaion/Atencion al Cliente')
	equipo = models.IntegerField(null=True,verbose_name='Trabajo en Equipo')
	compromiso = models.IntegerField(null=True,verbose_name='Compromiso')
	iniciativa = models.IntegerField(null=True,verbose_name='Iniciativa')
	id_evaluando = models.ForeignKey(empleado, on_delete=models.CASCADE)
	

	


	def resultado(self):
		return round((self.asistencia + self.puntualidad + self.presencia + self.cliente + self.equipo + self.compromiso + self.iniciativa)/7,2)




	



	class Meta:
		verbose_name='evalua'
		verbose_name_plural='evaluan'
		

	
class tarjeta(models.Model):
	id = models.AutoField(primary_key=True)
	p_nombre = models.CharField(max_length=100,blank=False, verbose_name='Primer Nombre')
	s_nombre = models.CharField(max_length=100,blank=True, verbose_name='Segundo Nombre')
	p_apellido = models.CharField(max_length=100,blank=False, verbose_name='Primer Apellido')
	s_apellido = models.CharField(max_length=100,blank=True, verbose_name='Segundo Apellido')
	lugar = models.ForeignKey(local, on_delete=models.CASCADE)


	class Meta:
	    verbose_name='tarjeta'
	    verbose_name_plural='tarjetas'
	    ordering=['p_apellido']	
