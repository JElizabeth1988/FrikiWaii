from django import forms
from django.forms import ModelForm
from .models import Producto, Categoria, Contacto, TipoContacto

class ProductoForm(ModelForm):

    codigo = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Ingrese un código'}), required=True, min_length=3, max_length=20, label='*Código')
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Ingrese un nombre'}), required=True, min_length=3, max_length=40, label='*Nombre' )
    descripcion = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder':'Ingrese descripción','rows':5, 'cols':20.8}), required=True, min_length=8, max_length=300, label='*Descripción')
    precio = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder':'Ingrese el precio'}), required=True, min_value=10, label='*Precio')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all() ,empty_label=None, label='*Categoría')
    
    class Meta:
        model = Producto
        fields = ['codigo','nombre','descripcion','precio','categoria','imagen']

class ContactoForm(ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Ingrese su nombre'}), required=True, min_length=3, max_length=50, label='*Nombre')
    apellido = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Ingrese su apellido'}), required=True, min_length=3, max_length=50, label='*Apellido' )
    asunto = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Ingrese un asunto'}), required=True, min_length=8, max_length=50, label='*Asunto')
    tipoContacto = forms.ModelChoiceField(queryset=TipoContacto.objects.all() ,empty_label=None, label='*Tipo de Contacto')
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder':'Ingrese su mensaje','rows':4, 'cols':20}), required=True, min_length=10, max_length=200, label='*Mensaje')


    class Meta:
        model = Contacto 
        fields = ['nombre','apellido','asunto','tipoContacto','mensaje']