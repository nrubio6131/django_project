from django.shortcuts import render
from django.http import HttpResponse
from primer_app.models import tabla

def formulario(request):
    return render(request,'form.html')
    
def envio_datos(request):

    if request.GET['nombre']:

        nombre= request.GET['nombre']
        personas = tabla.objects.filter(nombre__icontains = nombre)
        ctx={"nombre":nombre,"personas":personas}
        return render(request, "resultado.html",ctx)


        # mensaje = "busqueda: {}".format(request.GET["nombre"])
    else:
        mensaje = "no has introducido nada"
    return HttpResponse(mensaje)       


# Create your views here.

