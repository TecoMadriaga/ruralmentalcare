from django.contrib import admin

# Register your models here.
from .models import Paciente, Profesional, Cita, RecursoEducativo, Admin

admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Cita)
admin.site.register(RecursoEducativo)
admin.site.register(Admin)

