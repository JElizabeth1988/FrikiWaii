from rest_framework import serializers
from .models import Categoria, Producto

#--------------------------Clases Serializadoras--------------------------

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre','descripcion']

#----------------------------------------------------------------------------

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','descripcion','precio','categoria']