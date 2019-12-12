from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to="productos" , null= True, blank=True)

    def __str__(self):
        return self.nombre

class TipoContacto(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    tipoContacto = models.ForeignKey(TipoContacto, on_delete= models.CASCADE)
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
