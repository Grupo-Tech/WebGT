from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResources(resources.ModelResource):
	class Meta:
		model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre','estado','fecha_creacion',)
	resource_class = CategoriaResources

class AutorResource(resources.ModelResource):
	class Meta:
		model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['nombres','apellidos','correo']
	list_display = ('nombres','apellidos','correo','estado','fecha_creacion',)
	resource_class = AutorResource

class PostResource(resources.ModelResource):
	class Meta:
		model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['titulo','autor','categoria']
	list_display = ('titulo','autor','categoria','estado','fecha_creacion',)
	resource_class = PostResource


class ContactoResource(resources.ModelResource):
	class Meta:
		model = Contacto

class ContactoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['nombre','correo','asunto']
	list_display = ('nombre','correo','asunto',)
	resource_class = ContactoResource


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Contacto,ContactoAdmin)