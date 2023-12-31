from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Usuarios
from .forms import RegistrarUsuariosForm



class RegistrarUsuario(CreateView):
    model = Usuarios
    template_name = 'usuarios/registrar.html'
    form_class = RegistrarUsuariosForm
    success_url = reverse_lazy('inicio')

def ListarUsuarios(request):
    usuarios = Usuarios.objects.all()
    template_name = 'usuarios/listar_usuarios.html'
    contexto = {
        "usuarios": usuarios
    }
    return render(request,template_name,contexto)