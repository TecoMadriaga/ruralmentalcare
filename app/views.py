from django.shortcuts import render, get_object_or_404, redirect
from .models import Profesional, Cita, RecursoEducativo
from django.contrib.auth.decorators import login_required
from .forms import CitaForm

# Vista para listar profesionales
def lista_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'profesionales.html', {'profesionales': profesionales})

# Vista para ver detalles de un profesional
def detalle_profesional(request, pk):
    profesional = get_object_or_404(Profesional, pk=pk)
    return render(request, 'detalle_profesional.html', {'profesional': profesional})

# Vista para agendar una nueva cita
@login_required
def nueva_cita(request, profesional_id):
    profesional = get_object_or_404(Profesional, pk=profesional_id)
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.paciente = request.user.paciente
            cita.profesional = profesional
            cita.save()
            return redirect('detalle_cita', pk=cita.pk)
    else:
        form = CitaForm()
    return render(request, 'nueva_cita.html', {'form': form, 'profesional': profesional})

# Vista para listar recursos educativos
def lista_recursos(request):
    recursos = RecursoEducativo.objects.all()
    return render(request, 'recursos.html', {'recursos': recursos})
