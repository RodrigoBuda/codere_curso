from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
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


