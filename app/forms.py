from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TimeInput
from .models import Cita, Profesional, Paciente

class CitaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        label="Paciente",
        required=True
    )
    profesional = forms.ModelChoiceField(
        queryset=Profesional.objects.all(),
        label="Profesional",
        required=True
    )
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de inicio",
    )
    fecha_inicio_hora = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time', 'step': '60'}),
        label="Hora de inicio",
        help_text="Formato: HH:MM"
    )
    class Meta:
        model = Cita
        # fields = ['paciente', 'profesional', 'fecha_hora_inicio', 'fecha_hora_fin', 'estado', 'resumen']
        fields = ['paciente', 'profesional', 'fecha_inicio', 'fecha_inicio_hora']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'profesional': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_inicio_hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    