from django.test import TestCase, Client
from django.urls import reverse
from .models import Producto, Categoria
from .views import registro
import json

# Create your tests here.
class BasicTest(TestCase):

     def test_registro(self):
        producto = Producto()
        producto.codigo = "AA12"
        producto.nombre = "audifonos"
        producto.descripcion = "para escuchar música"
        producto.precio = 2000
        producto.categoria = "accesorios"
        producto.imagen = null
        producto.save()

        record = Producto.objects.get(pk="AA12")
        self.assertEqual(record,producto)


    def test_listado(self):
        Producto = Producto()

        response = Producto.get(reverse('lista'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'core/listado.html')

