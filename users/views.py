from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import UserForm


def login_view(request):
    template_name = 'users/login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('')
        else:
            messages.error(request, 'Usuario o Contraseña invalidos')

    return render(request, template_name)


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('users:login')


def register(request):
    template_name = 'users/register.html'
    form = UserForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(
                request, f'El usuario {user.username} ha sido creado exitosamente'
            )
            return redirect('')

    return render(request, template_name, {
        'form': form,
    })
