from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group,Permission
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
    permiso = Permission.objects.all()
    usuarios = User.objects.all()
    grupos = Group.objects.all()
    contexto = {
        'usuarios':usuarios,
        'permiso': permiso,
        'grupos': grupos
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
            messages.success(request, "Se registró la noticia con éxito.") 
            return redirect('admi')   
        except Exception as e:
            messages.error(request, f"Error al cargar la Noticia: {e}") 
            return redirect('add_noticia') 
        
    return render(request, "paginas/noticia.html")

def solicitud_soport(request):
    consulta = Area.objects.all()
    contexto = {
        'consulta': consulta
    }
    
    if request.method == 'POST':
        
        are = request.POST.get('area')
        asunto = request.POST.get('asunto')
        descrip = request.POST.get('descripcion')
        status = request.POST.get('status', '3')
        level = request.POST.get('level', '3')
        
        area_id_entero = int(are) 
        if request.user.is_authenticated:
            reportero = request.user
        else:
            return HttpResponseForbidden("Debes iniciar sesión para enviar un reporte.")
        try:
            new_report = Report.objects.create(
                TITLE = asunto,
                descripcion = descrip,
                area_id = area_id_entero ,
                reporter_user = reportero,
                STATUS_id = status,
                ID_LEVEL_id = level
            )
            new_report.save()
            messages.success(request, "Su solicitud de soporte ha sido enviada con éxito.")
            return redirect('solicitud_soport')
        except Exception as e:
            messages.error(request, f"Error al enviar la solicitud de soporte: {e}")
            return redirect('solicitud_soport')
    
    return render(request, "paginas/solicitud_soport.html", contexto)

def soporte(request):
    casos = Report.objects.all()
    status = Status.objects.all()
    level = Level.objects.all()
    tecnico = User.objects.all()
    contexto = {
        'casos': casos,
        'status': status,
        'level': level,
        'tecnico': tecnico

    }
    return render(request, "paginas/soporte.html",contexto)

def registrar_usuarios(request):
    if request.method == 'POST':
        first_name = request.POST.get('nombre')
        last_name = request.POST.get('apellido')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        grupo_id = request.POST.get('grupo')
        
        try:
            
            new = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            grupo = Group.objects.get(id=grupo_id)
            new.groups.add(grupo)
            new.save()
            messages.success(request, "Usuario registrado con éxito.")
            return redirect('usuario')
        except Exception as e:
            messages.error(request, f"Error al registrar el usuario: {e}")
            return redirect('usuario')
    else:
        messages.error(request, "Método no permitido para registrar usuario.")
        return redirect('usuario')

def registrar_rol(request):
        if request.method == 'POST':
            grupo_nombre = request.POST.get('grupo')
            permisos_ids = request.POST.getlist('permisos')
            
            try:
                nuevo_grupo = Group.objects.create(name=grupo_nombre)
                
                for perm_id in permisos_ids:
                    permiso = Permission.objects.get(id=perm_id)
                    nuevo_grupo.permissions.add(permiso)
                
                nuevo_grupo.save()
                messages.success(request, "Rol registrado con éxito.")
                return redirect('usuario')
            except Exception as e:
                messages.error(request, f"Error al registrar el rol: {e}")
                return redirect('usuario')
        else:
            messages.error(request, "Método no permitido para registrar rol.")
            return redirect('usuario')

def eliminar_usuario(request, user_id):
    if request.method == 'POST':
        try:
            user_to_delete = User.objects.get(id=user_id)
            user_to_delete.delete()
            messages.success(request, "Usuario eliminado con éxito.")
            return redirect('usuario')
        except User.DoesNotExist:
            messages.error(request, "El usuario no existe.")
            return redirect('usuario')
        except Exception as e:
            messages.error(request, f"Error al eliminar el usuario: {e}")
            return redirect('usuario')
    else:
        messages.error(request, "Método no permitido para eliminar usuario.")
        return redirect('usuario')

def editar_usuario(request, user_id):
    if request.method == 'POST':
        try:
            user_to_edit = User.objects.get(id=user_id)
            user_to_edit.username =  request.POST.get('username', user_to_edit.username)
            user_to_edit.first_name = request.POST.get('first_name', user_to_edit.first_name)
            user_to_edit.last_name = request.POST.get('last_name', user_to_edit.last_name)
            user_to_edit.email = request.POST.get('email', user_to_edit.email)
            password = request.POST.get('password')
            if password:
                user_to_edit.set_password(password)
            
            user_to_edit.save()
            messages.success(request, "Usuario actualizado con éxito.")
            return redirect('usuario')
        except User.DoesNotExist:
            messages.error(request, "El usuario no existe.")
            return redirect('usuario')
        except Exception as e:
            messages.error(request, f"Error al actualizar el usuario: {e}")
            return redirect('usuario')
    else:
        messages.error(request, "Método no permitido para editar usuario.")
        return redirect('usuario')


def exit(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('loggi')