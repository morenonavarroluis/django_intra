from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


def inicio(request):
    return render(request, "paginas/login.html")

def loggi(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user =  authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('admi')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrecta ')
            return render(request, "paginas/login.html")
        
    return render(request, "paginas/login.html")

def admi(request):
    return render(request, "paginas/administrador.html")

def usuario(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios':usuarios
    }
    return render(request, "paginas/usuario.html",contexto)