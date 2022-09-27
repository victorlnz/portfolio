from django.db import models

# Create your models here.

class Proyectos(models.Model):

    titulo = models.CharField("Titulo:", max_length=50)
    descripcion = models.CharField("Descripcion:", max_length=250)
    imagen = models.ImageField("Imagen:", upload_to="imagen-proyectos", height_field=None, width_field=None, max_length=None)
    url = models.URLField("URL:", max_length=200)

    class Meta:
        
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.titulo + "-" + self.url

class Correos(models.Model):

    nombre = models.CharField("Nombre Completo:", max_length=100)
    email = models.EmailField("Email:", max_length=250)
    mensaje = models.TextField("Mensaje:", max_length=250,)
    leido = models.BooleanField(default=False,blank=True)
    

    class Meta:
        
        verbose_name = "Correo"
        verbose_name_plural = "Correos"

    def __str__(self):
        return self.nombre + "-" + self.email




            
        
        