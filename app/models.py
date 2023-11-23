from django.db import models
from django.contrib.auth.models import User
from django import forms

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
    biografia = models.TextField()
    calificacion_promedio = models.FloatField(default=0.0)

    def __str__(self):
        return self.usuario.username
        
class Admin(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

# Modelo para citas
class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    estado = models.CharField(max_length=50)
    resumen = models.TextField(blank=True)

    def __str__(self):
        return f"Cita entre {self.paciente.usuario.username} y {self.profesional.usuario.username}"

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

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('fecha_hora_inicio', 'fecha_hora_fin', 'estado', 'resumen')
        labels = {
            'fecha_hora_inicio': 'Fecha y hora de inicio',
            'fecha_hora_fin': 'Fecha y hora de fin',
            'estado': 'Estado',
            'resumen': 'Resumen'
        }
        widgets = {
            'fecha_hora_inicio': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'fecha_hora_fin': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'})
        }