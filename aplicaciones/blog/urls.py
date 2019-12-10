from django.contrib import admin
from django.urls import path
from .views import *

admin.site.site_header = 'Grupo Tech'
admin.site.site_title = 'Grupo Tech'
admin.site.index_title = 'Administración'

urlpatterns = [
	path('admin/', admin.site.urls),
	path('',home, name = 'index'),
	path('acerca_de/',Acerca_de, name = 'acerca_de'),
	path('Clientes/',Clientes, name = 'Clientes'),
	path('Productos/',Productos, name = 'Productos'),
	path('Contactos/', FormularioContacto.as_view(), name = 'Contactos'),
]