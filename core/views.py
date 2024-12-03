from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import RegistroForm,LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from .models import UsuarioComun
from .forms import UsuarioPerfilForm, CustomPasswordChangeForm


class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'core/registro.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            if user.rol == 'agente':
                return redirect('inicio_agente')
            else:
                return redirect('inicio_usuario')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
        return render(request, 'core/registro.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'core/login.html', {'form': form})

    def post(self, request):
        user_type = request.POST.get('user_type', 'usuario')
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.rol != user_type:
                form.add_error(None, 'El tipo de usuario seleccionado no coincide con tu cuenta. Por favor, selecciona el tipo de usuario correcto.')
                return render(request, 'core/login.html', {'form': form})
            
            login(request, user)
            if user.rol == 'agente':
                return redirect('inicio_agente')
            else:
                return redirect('inicio_usuario')
        return render(request, 'core/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, '¡Has cerrado sesión exitosamente!')
        return redirect('login')

def inicio_agente(request):
    return render(request,'core/usuario_dashboard')

def inicio_agente(request):
    return render(request,'core/usuario_dashboard')
