from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Modelo para usuarios (pacientes)
class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    historial_medico = models.TextField(blank=True)

    def __str__(self):
        return self.usuario.username

# Modelo para profesionales
class Profesional(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    biografia = models.TextField(null=True, blank=True)
    calificacion_promedio = models.FloatField(default=0.0)
    imagen = models.URLField(default="https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png")

    def __str__(self):
        return self.usuario.username
        
class Admin(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

# Modelo para citas
from django.db import models
import datetime

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_inicio_hora = models.TimeField(default=datetime.time(0, 0))
    fecha_fin_hora = models.TimeField(default=datetime.time(0, 0))
    estado = models.CharField(max_length=50, default="Pendiente")
    resumen = models.TextField(blank=True ,null=True)

    def __str__(self):
        return f"Cita entre {self.paciente.usuario.username} y {self.profesional.usuario.username}"
    
    def save(self, *args, **kwargs):
        if not self.fecha_fin_hora:
            self.fecha_fin = self.fecha_inicio
            self.fecha_fin_hora = (datetime.datetime.combine(datetime.date(1, 1, 1), self.fecha_inicio_hora) + datetime.timedelta(hours=1)).time()
        super(Cita, self).save(*args, **kwargs)


# Modelo para recursos educativos
class RecursoEducativo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)
    enlace = models.URLField()
    fecha_publicacion = models.DateField(null=True, blank=True)
    imagen = models.URLField()

    def __str__(self):
        return self.titulo

# Modelo para feedback/reseñas
class Feedback(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f"Feedback de {self.paciente.usuario.username} sobre {self.profesional.usuario.username}"
