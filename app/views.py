from django.shortcuts import render, get_object_or_404, redirect
from .models import Profesional, Cita, RecursoEducativo, Paciente, CitaForm
from django.contrib.auth.decorators import login_required

# Vista para listar profesionales
def lista_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'profesionales.html', {'profesionales': profesionales})

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def registro(request):
    return render(request, 'registro.html')

def registro_profesional(request):
    return render(request, 'registro_profesional.html')

# Vista para ver detalles de un profesional
def detalle_profesional(request, pk):
    profesional = get_object_or_404(Profesional, pk=pk)
    return render(request, 'detalle_profesional.html', {'profesional': profesional})

# Vista para agendar una nueva cita
# @login_required
# def nueva_cita(request, profesional_id):
#     profesional = get_object_or_404(Profesional, pk=profesional_id)
#     if request.method == 'POST':
#         form = CitaForm(request.POST)
#         if form.is_valid():
#             cita = form.save(commit=False)
#             cita.profesional = profesional
#             cita.paciente = request.user  # Asumiendo que el paciente está logueado
#             cita.save()
#             # Redirigir a una nueva URL:
#             return HttpResponseRedirect('/cita_exitosa/')
#     else:
#         form = CitaForm()
#     return render(request, 'nueva_cita.html', {'form': form, 'profesional': profesional})
def nueva_cita(request):
    return render(request, 'nueva_cita.html')
# Vista para listar recursos educativos
def lista_recursos(request):
    recursos = RecursoEducativo.objects.all()
    return render(request, 'recursos.html', {'recursos': recursos})