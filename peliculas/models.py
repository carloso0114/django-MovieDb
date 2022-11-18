from django.db import models

# Create your models here.
class Director(models.Model):
  name = models.CharField(max_length=64, help_text='Pon el nombre del director')
  fechaNacimiento = models.DateField(null=True)
  def __str__(self):
    return self.name

class Pelicula(models.Model):
  title = models.CharField(max_length=32)
  author = models.ManyToManyField(Director)
  summary = models.TextField(max_length=100, help_text='Sipnosis', null=True)
  year = models.DateField(null=True)

  def __str__(self):
    return self.title