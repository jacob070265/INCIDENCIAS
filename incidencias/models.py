from django.db import models

# Create your models here.

class Linea (models.Model): 
    nombre = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    distancia = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
    
class Estacion (models.Model): 
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nombre
    
class Incidencia (models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField()
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.estacion} ({self.estacion.linea})'
    