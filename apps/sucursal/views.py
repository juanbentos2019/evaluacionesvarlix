from django.shortcuts import render, render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib import auth, messages
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import evaluaForm, empleadoForm, localForm, tarjetaForm
from .models import empleado, evalua, local, tarjeta
from django.db.models import Q


def Home(request):
	return render(request, 'index.html')


def welcome(request):
    return render(request, "users/welcome.html")

def register(request):
    return render(request, "users/register.html")

def login(request):
    return render(request, "users/login.html")


def logout(request):
    # Redireccionamos a la portada
    return redirect('/')




def CrearEvaluacion(request):
	if request.method =='POST':
		evalua_form = evaluaForm(request.POST)
		if evalua_form.is_valid():
			evalua_form.save()
			return redirect('index')

	else:
		evalua_form = evaluaForm()
	return render(request,'sucursal/crear_evaluacion.html',{'evalua_form':evalua_form})

def CrearEmpleado(request):
	if request.method =='POST':
		empleado_form = empleadoForm(request.POST)
		if empleado_form.is_valid():
			empleado_form.save()
			return redirect('index')

	else:
		empleado_form = empleadoForm()
	return render(request, 'sucursal/crear_empleado.html',{'empleado_form':empleado_form})


def listar_Empleado(request):
	empleados = empleado.objects.all()
	return render(request,'sucursal/listar_empleado.html',{'empleados':empleados})

def listar_Evaluacion(request):
	evaluaciones = evalua.objects.all()
	return render(request,'sucursal/listar_evaluacion.html',{'evaluaciones':evaluaciones})
	

def editar_Empleado(request,id):
	error = None
	empleado_form = None
	try:
		empleadoe = empleado.objects.get(id = id)
		if request.method == 'GET':
			empleado_form = empleadoForm(instance = empleadoe)
		else:
			empleado_form = empleadoForm(request.POST, instance = empleadoe)
			if empleado_form.is_valid():
				empleado_form.save()
			return redirect('sucursal:listar_empleado')
	except ObjectDoesNotExist as e:
		error = e
	
	return render(request, 'sucursal/crear_empleado.html',{'empleado_form':empleado_form,'error':error})

def eliminar_Empleado(request, id):
	empleadofue = empleado.objects.get(id = id )
	empleadofue.delete()
	return redirect('sucursal:listar_empleado')

def Crear_Local(request):
	if request.method =='POST':
		local_form = localForm(request.POST)
		if local_form.is_valid():
			local_form.save()
			return redirect('index')
	else:
		local_form = localForm()
	return render(request, 'sucursal/crear_local.html',{'local_form':local_form})		

def listar_Local(request):
	locales = local.objects.all()
	return render(request, 'sucursal/listar_local.html',{'locales':locales})

def Crear_Tarjeta(request):
	if request.method =='POST':
		tarjeta_form = tarjetaForm(request.POST)
		if tarjeta_form.is_valid():
			tarjeta_form.save()
			return redirect('sucursal:listar_tarjetas')
	else:
		tarjeta_form = tarjetaForm()
	return render(request, 'sucursal/crear_tarjeta.html',{'tarjeta_form':tarjeta_form})

def listar_Tarjetas(request):
	queryset = request.GET.get("buscar")
	tarjetas = tarjeta.objects.filter()
	if queryset:
		tarjetas = tarjeta.objects.filter(
                Q(p_nombre__icontains = queryset) |
                Q(s_nombre__icontains = queryset) |
                Q(p_apellido__icontains = queryset) |
                Q(s_apellido__icontains = queryset) 
			).distinct()
	return render(request,'sucursal/ver_tarjetas.html',{'tarjetas':tarjetas})

def eliminar_Tarjeta(request, id):
	tarjetafue = tarjeta.objects.get(id = id )
	tarjetafue.delete()
	return redirect('sucursal:listar_tarjetas')
