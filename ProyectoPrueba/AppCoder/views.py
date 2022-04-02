from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template import loader
from .models import Curso, Familia, Profesor
from AppCoder.models import Profesor

# Create your views here.

def curso(request,nombre,camada):
    micurso=Curso(nombre=nombre,camada=camada)
    micurso.save()
    #return HttpResponse(f"se genero curso {micurso.nombre} y la camada {micurso.camada}")
    return render(request, "appcoder/cursos.html", {"nombre": nombre, "camada":camada})

def profesor(request,nombre,apellido, email,profesion):
    profe=Profesor(nombre=nombre,apellido=apellido,email=email, profesion=profesion)
    profe.save()
    return HttpResponse(f"se agrego el profesor {profe.nombre} , {profe.apellido}")

def recuperar_profesor(request):
    profe=Profesor.objects.all()
 
    #contexto= Context({"p":profe})
    return render(request,"template2.html",{"profe":profe})


def recuperar_curso(request):
    curso=Curso.objects.all()
 
    #contexto= Context({"p":profe})
    return render(request,"template_cursos.html",{"curso":curso})
    
def probandotemplate(request):

    listaNotas =[1,4,8,10,20] 
    mihtml= open(r"C:\Users\usuario\Documents\proyecto_coder\ProyectoPrueba\ProyectoPrueba\templates\template1.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    contexto= Context({"notas":listaNotas})
    return HttpResponse(plantilla.render(contexto))

def profesores(request):
    return render(request,"appcoder/profesores.html")
    #return HttpResponse("vista de profesores")

def estudiantes(request):
    return render(request,"appcoder/estudiantes.html")

def entregables(request):
    return render(request,"appcoder/entregables.html")

def inicio(request):
    return render(request,"appcoder/inicio.html")
 
#agregar familiares
def agregafamiliar(request,nombre,apellido, dni,fecha_nacimiento):
    familiar=Familia(nombre=nombre,apellido=apellido,dni=dni,fecha_nacimiento=fecha_nacimiento)
    familiar.save()
    return HttpResponse(f"se agrego el familiar {familiar.nombre} , {familiar.apellido}")

def recuperar_familia(request):
    familia=Familia.objects.all()
 
    #contexto= Context({"p":profe})
    return render(request,"template_familia.html",{"familia":familia})