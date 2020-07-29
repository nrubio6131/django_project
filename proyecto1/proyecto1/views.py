from django.http import HttpResponse
import datetime
from django.template import Template, Context

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
#para cargar el template
    doc_externo=open('D:/OneDrive - Universidad de San Buenaventura - Bogota/nick/Repositorios/django_project/proyecto1/proyecto1/templates/fst_template.html')
#crear el objeto tipo template
    tmplt=Template(doc_externo.read())
#se cierra la comunicacion una vezx cargado el template
    doc_externo.close()
#se cera un contexto
    ctx=Context()
#se renderiza el objeto creado
    doc=tmplt.render(ctx)
#se imporime el objeto renderizado, para mostrar el contenido del template, de lo contrario retornara none
    return(HttpResponse(doc))


