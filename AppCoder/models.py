from django.db import models

<<<<<<< HEAD
class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
=======
# Create your models here.

class Vendedor(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Vendedores'
>>>>>>> 0700b2c480ce15c9ab23972ea956a2196f857578
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre + '(' + self.apellido +')'
    
class Compra(models.Model):
    producto = models.CharField(max_length=30)
    precio = models.IntegerField()
    enviado = models.BooleanField()

    def __str__(self):
        return self.producto
<<<<<<< HEAD


=======
    
>>>>>>> 0700b2c480ce15c9ab23972ea956a2196f857578
