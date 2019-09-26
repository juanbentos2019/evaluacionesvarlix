"""evaluador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from apps.sucursal.views import Home, CrearEvaluacion, CrearEmpleado, listar_Empleado, listar_Evaluacion, editar_Empleado, eliminar_Empleado, listar_Local, Crear_Local, Crear_Tarjeta, listar_Tarjetas, eliminar_Tarjeta



urlpatterns = [
    path('admin/', admin.site.urls),
    path('sucursal/',include(('apps.sucursal.urls','sucursal'))),
    path('home/', login_required(Home), name='index'),
    path('accounts/login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('sucursal/crear_evaluacion/', CrearEvaluacion, name='crear_evaluacion'),
    path('sucursal/crear_empleado/', CrearEmpleado, name='crear_empleado'),
    path('sucursal/listar_empleado/', listar_Empleado, name='listar_empleado'),
    path('sucursal/listar_evaluacion/', listar_Evaluacion, name='listar_evaluacion'),
    path('sucursal/editar_empleado/', editar_Empleado, name='editar_empleado'),
    path('sucursal/eliminar_empleado/',eliminar_Empleado, name='eliminar_empleado'),
    path('sucursal/crear_local',Crear_Local, name='crear_local'),
    path('sucursal/listar_local/',listar_Local, name='listar_local'),
    path('sucursal/crear_tarjeta/',Crear_Tarjeta, name='crear_tarjeta'),
    path('sucursal/listar_tarjetas/',listar_Tarjetas, name='listar_tarjetas'),
    path('sucursal/eliminar_tarjeta/',eliminar_Tarjeta, name='eliminar_tarjeta')
]
