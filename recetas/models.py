from django.db import models


class Receta(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    precio = models.FloatField(default=0)

    def __unicode__(self):
        return self.nombre


class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta)
    materia_prima = models.ForeignKey(MateriaPrima)
    cantidad = models.FloatField(default=0)

    def __unicode__(self):
        return self.cantidad
