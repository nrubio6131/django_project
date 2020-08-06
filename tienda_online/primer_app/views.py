from django.shortcuts import render
from django.http import HttpResponse
from primer_app.models import tabla
from django.core.mail import send_mail
from django.conf import settings

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

def contacto(request):
    if request.method == 'POST': 
        ctx={'token':'Enviado satisfactoriamente'}
        subject = request.POST['asunto']
        message = '{} \nEl mensaje ha sido enviado desde {}'.format(request.POST['motivos'],request.POST['email'])
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['darknick6131@gmail.com']
        
        send_mail(subject,message,from_email,recipient_list)
    else:
        ctx={'token':'No se ha enviado nada'}

    return render(request, "contacto.html",ctx)

def envio_contacto(request):
    asunto= request.POST['asunto']
    email= request.POST['email']
    motivos= request.POST['motivos']
    mensaje='''{} <br>
    {}<br>
    {}'''.format(
        asunto,
        email,
        motivos)
    return HttpResponse(mensaje)  
# Create your views here.

