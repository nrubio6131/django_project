from django.db import models

class tabla (models.Model):
    nombre= models.CharField(max_length= 50)
    apellido= models.CharField(max_length=50)
    profesion= models.CharField(max_length=30)
    correo=models.EmailField()
    edad=models.IntegerField()
    fecha_creacion= models.DateField()
    activo=models.BooleanField()

    def __str__(self):
        return """el resultado de la consulta es el siguiente :
        
        nombre: {} 
        apellido: {} 
        profesion: {} 
        correo: {} 
        edad: {} 
        fecha de creacion: {} 
        activo?: {} 
        """.format(
            self.nombre,
            self.apellido,
            self.profesion,
            self.correo,
            self.edad,
            self.fecha_creacion,
            self.activo)

class prueba (models.Model):
    colum1= models.CharField(max_length=50)
    colum2= models.CharField(max_length=50)
    colum3= models.CharField(max_length=50)
# Create your models here.
