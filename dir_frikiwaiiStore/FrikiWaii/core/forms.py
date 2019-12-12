from django import forms
from django.forms import ModelForm
from .models import Producto, Contacto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','descripcion','precio','categoria','imagen']

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto 
        fields = ['nombre','apellido','asunto','tipoContacto','mensaje']