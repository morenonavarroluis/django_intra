from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


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
    noticias = Imagenes.objects.all()
    contexto = {
        'noticias':noticias
    }
    return render(request, "paginas/administrador.html",contexto)

def usuario(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios':usuarios
    }
    return render(request, "paginas/usuario.html",contexto)

def add_noticia(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
     
        content = request.POST.get('contenido')
    
        img = request.FILES.get('imagen')
        try:
            new_noticia = Imagenes.objects.create(
             nombre=title,
             comentario=content,
             imagen=img
             )
            new_noticia.save()
            messages.success("Se registro la noticias con exito")
            return redirect('admi')
        except Exception as e:
            messages.error(request, "Error al cargar la Noticia")
            return redirect('add_noticia') 
    return render(request, "paginas/noticia.html")

def soporte(request):
    return render(request, "paginas/soporte.html")