from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CitaForm, UserForm
from .models import Cita
from .models import Profesional, Cita, RecursoEducativo, Paciente
from django.contrib.auth.models import Group

@login_required
def crear_cita(request):
    formulario = CitaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Cita creada con éxito.')
        return redirect('index')
    else:
        messages.error(request, 'Error al crear la cita.')

    return render(request, 'nueva_cita.html', {'formulario': formulario})

@login_required
def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    formulario = CitaForm(request.POST or None, instance=cita)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Cita editada con éxito.')
        return redirect('index')
    return render(request, 'editar_cita.html', {'formulario': formulario})

# Vista para listar profesionales
def lista_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'profesionales.html', {'profesionales': profesionales})

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                datos = { 'usuario': user, 'mensaje': f'Bienvenido {user.username}!', 'info': 'login'}
                return render(request, 'index.html', datos)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirigir a una página de inicio exitoso, por ejemplo, el dashboard del usuario
                return redirect('index')
            else:
                # Manejar usuarios que están deshabilitados o inactivos
                return render(request, 'login.html', {'error': 'Tu cuenta está desactivada.'})
        else:
            # Manejar credenciales incorrectas
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        # Mostrar la página de inicio de sesión si no es una solicitud POST
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    datos = { 'info': 'logout', 'mensaje': 'Has cerrado sesión exitosamente.'}
    return render(request, 'index.html', datos)

def registro(request):
    formulario = UserForm(request.POST or None)
    if formulario.is_valid():
        user = formulario.save()  # Guardar el usuario y obtener la instancia

        # Asignar al grupo
        grupo_nombre = 'Paciente'
        grupo, created = Group.objects.get_or_create(name=grupo_nombre)
        user.groups.add(grupo)

        messages.success(request, 'Usuario creado con éxito.')
        return redirect('index')
    else:
        messages.error(request, 'Error al crear el usuario.')

    return render(request, 'registro.html', {'formulario': formulario})

def registro_profesional(request):
    return render(request, 'registro_profesional.html')

# Vista para ver detalles de un profesional
def detalle_profesional(request, pk):
    profesional = get_object_or_404(Profesional, pk=pk)
    return render(request, 'detalle_profesional.html', {'profesional': profesional})


def nueva_cita(request):
    return render(request, 'nueva_cita.html')
# Vista para listar recursos educativos
def lista_recursos(request):
    recursos = RecursoEducativo.objects.all()
    return render(request, 'recursos.html', {'recursos': recursos})

def lista_citas(request):
    try:
        # If user is patient, show their appointments
        if request.user.groups.filter(name='paciente').exists():
            paciente = Paciente.objects.get(usuario=request.user)
            citas = Cita.objects.filter(paciente=paciente).order_by('fecha_inicio')
        # If user is professional, show their appointments
        elif request.user.groups.filter(name='profesional').exists():
            profesional = Profesional.objects.get(usuario=request.user)
            citas = Cita.objects.filter(profesional=profesional).order_by('fecha_inicio')
    except Paciente.DoesNotExist:
        messages.info(request, 'No se encontró el perfil de paciente asociado.')
        citas = Cita.objects.none()  # No hay citas
    except Profesional.DoesNotExist:
        messages.info(request, 'No se encontró el perfil de profesional asociado.')
        citas = Cita.objects.none()

    # Paginación
    paginator = Paginator(citas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'citas_agendadas.html', {'citas': page_obj})
    