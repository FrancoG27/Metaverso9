from .models import Usuarios
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm



class RegistrarUsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','apellido','fecha_nacimiento','username','password','password2','email','imagen']
