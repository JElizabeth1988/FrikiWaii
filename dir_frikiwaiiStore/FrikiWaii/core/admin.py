from django.contrib import admin
from .models import Producto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','precio','categoria')
    search_fields = ['codigo','nombre']
    list_filter = ('categoria',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'descripcion')
    search_fields = ['nombre','descripcion']
    list_filter = ('nombre',)

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)

