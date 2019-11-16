from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)

class Producto(models.Model):
    código = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    # imagen = models.ImageField(upload_to="automoviles" , null= True )