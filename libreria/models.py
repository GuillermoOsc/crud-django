from distutils.command.upload import upload
from re import T
from django.db import models

# Create your models here.


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(
        upload_to='imagenes/', verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)

# La siguiente función muestra los datos ( titulo y descripción) de los libros en el admin de Django

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila

# Función para borrado de imagenes de cada libro

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
