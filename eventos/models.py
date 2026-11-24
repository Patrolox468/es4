from django.db import models


class Evento(models.Model):
    nombre = models.CharField(max_length=120)
    lugar = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    valor = models.PositiveIntegerField(help_text="Valor de la entrada en pesos")
    cupos = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    def _str_(self):
        return self.nombre

    def cupos_disponibles(self):
        ocupados = sum(i.cantidad for i in self.inscripciones.all())
        return self.cupos - ocupados


class Inscripcion(models.Model):
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name="inscripciones",
    )
    nombre = models.CharField(max_length=120)
    correo = models.EmailField()
    cantidad = models.PositiveIntegerField(default=1)
    creada = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.nombre} en {self.evento}"