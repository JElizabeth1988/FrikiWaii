from django.contrib import admin
from .models import Producto, Categoria, Contacto, TipoContacto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','precio','categoria')
    search_fields = ['codigo','nombre']
    list_filter = ('categoria',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'descripcion')
    search_fields = ['nombre','descripcion']
    list_filter = ('nombre',)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','asunto','tipoContacto','mensaje')
    search_fields = ['nombre','apellido']
    list_filter = ('tipoContacto',)

class TipoContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre',] 
    list_filter = ('nombre',)   

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contacto ,ContactoAdmin)
admin.site.register(TipoContacto, TipoContactoAdmin)

