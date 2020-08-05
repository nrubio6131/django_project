from django.db import models

class tabla (models.Model):
    nombre= models.CharField(max_length= 50,null=True,blank=True,verbose_name="Name")
    apellido= models.CharField(max_length=50,verbose_name="Last name")
    profesion= models.CharField(max_length=30,verbose_name="career")
    correo=models.EmailField(verbose_name="E-mail")
    edad=models.IntegerField(verbose_name="Age")
    fecha_creacion= models.DateField(verbose_name="Date created")
    activo=models.BooleanField(verbose_name="Active?")

    def __str__(self):
        return """
        nombre: {}, 
        apellido: {}, 
        profesion: {}, 
        correo: {},
        edad: {},
        fecha de creacion: {},
        activo?: {},
        """.format(
            self.nombre,
            self.apellido,
            self.profesion,
            self.correo,
            self.edad,
            self.fecha_creacion,
            self.activo)

class prueba (models.Model):
    colum1= models.CharField(max_length=50,default="none")
    colum2= models.CharField(max_length=50)
    colum3= models.CharField(max_length=50)

    def __str__(self):
        return 'id={},{},{},{}'.format(self.id,self.colum1,self.colum2,self.colum3)
# Create your models here.
