from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CrearEvaluacion, CrearEmpleado, listar_Empleado, listar_Evaluacion, editar_Empleado, eliminar_Empleado, listar_Local, Crear_Local, Crear_Tarjeta, listar_Tarjetas, eliminar_Tarjeta

urlpatterns = [
path('crear_evaluacion/',login_required(CrearEvaluacion), name ='crear_evaluacion'),
path('crear_empleado/',login_required(CrearEmpleado), name='crear_empleado'),
path('listar_empleado/',login_required(listar_Empleado), name='listar_empleado'),
path('listar_evaluacion/',login_required(listar_Evaluacion), name='listar_evaluacion'),
path('editar_empleado/<int:id>',login_required(editar_Empleado), name='editar_empleado'),
path('eliminar_empleado/<int:id>',login_required(eliminar_Empleado), name='eliminar_empleado'),
path('crear_local/',login_required(Crear_Local), name='crear_local'),
path('listar_local/',login_required(listar_Local), name='listar_local'),
path('crear_tarjeta/',login_required(Crear_Tarjeta), name='crear_tarjeta'),
path('listar_tarjetas/',login_required(listar_Tarjetas), name='listar_tarjetas'),
path('eliminar_tarjeta/<int:id>',login_required(eliminar_Tarjeta), name='eliminar_tarjeta')
]