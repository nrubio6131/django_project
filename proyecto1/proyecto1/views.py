from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
        def __init__(self,nombres,apellidos):

            self.nombres=nombres

            self.apellidos=apellidos

def inicio(request):

    return HttpResponse("Primera vista creada con Django")

def fin(request):
    
    return HttpResponse("esta pagina finaliza el tutorial 2")

def fecha(request):
    FechaActual=datetime.datetime.now()
    return HttpResponse("la fehca actual es:{}".format(FechaActual))

def MetodoGet(request,v1,v2):
    return HttpResponse("""
    <html>
    <body>
    <h2>
    Esto es un texto de prueba con formato <br>
    </h2>
    La variable 1 es un nuemor y es: {} <br>
    La variable 2 es una cadena y es: {} <br>
    
    </body>
    </html>
    """.format(v1,v2))

def vista(request):

    return render(request,'fst_template.html')

def vista_con_parametros(request):
    nombre='Nicolás'
    apellido='Rubio'
    fecha=datetime.datetime.now()
    prueba_objeto=Persona("Nicolas Emilio","Rubio Aparicio")
    lista=['torre',
    'fuente',
    'monitor',
    'tecaldo',
    'mouse',
    'targeta madre',
    'procesador',
    'targeta grafica',
    'memoria ram',
    'disco duro']

    #tmplt=get_template('template_variables.html')
    ctx={"nombre":nombre, "apellido":apellido, "fecha":fecha, "persona":prueba_objeto,"partes_pc":lista}
    #doc=tmplt.render(ctx)
    #return(HttpResponse(doc))
    return render (request,'template_variables.html',ctx)

def video(request):
    creador = Persona("Nicolas Emilio","Rubio Aparicio")
    ctx={"creador":creador}
    return render(request,'videos.html',ctx)

def plantilla_hija_2(request):
    creador = Persona("Pepito","Peréz")
    ctx={"creador":creador}
    return render(request,'plantilla_hija_2.html',ctx)
