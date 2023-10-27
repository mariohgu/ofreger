
from django.http import HttpResponse
import datetime
from django.template import Template, Context


#Request: Realizar peticiones al servidor

#HTTPResponse: Respuesta del servidor

#Esto es una vista
def bienvenida(request):
    return HttpResponse("bienvenida")

def bienvenidaRojo(request):
    return HttpResponse("<b style='color:red'>Hola como estas</b>")

def categoriaEdad(request, edad):
    if edad < 18:
        categoria = "Es menor de edad"
    else:
        categoria = "Es mayor de edad"
    
    resultado = f"<h1>Tu categoria es: {categoria}<h1>"
    return HttpResponse(resultado)

def obtenermomentoactual(request):
    respuesta = f"<h1>Momento actual: {datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S')}<h1>"
    return HttpResponse(respuesta)
    
def contenidoHTML(request, nombre, edad):
    contenido = f"""
    <html>
    <body>
        <h1 style='color:blue'>Nombre: {nombre}</h1>
        <h1>Edad: {edad}</h1>
    </body>
    </html>
    """
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    #Abrimos el documento que contiene la plantilla
    plantillaExterna = open("/home/wario/Documentos/Coding/ofreger/peligros/peligros/plantillas/miPrimeraPlantilla.html")
    #carga el documento den una variable de tipo Plantilla
    template = Template(plantillaExterna.read())
    #cerrar el documento
    plantillaExterna.close()
    #crear una variable de tipo Context
    contexto = Context()
    #renderizar la plantilla
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaParametros(request):
    #Abrimos el documento que contiene la plantilla
    plantillaParametros = open("/home/wario/Documentos/Coding/ofreger/peligros/peligros/plantillas/plantillaParametros.html")
    nombre = 'Mario'
    fechaActual = datetime.datetime.now()
    plantilla = Template(plantillaParametros.read())
    plantillaParametros.close()
    contexto = Context({'nombreUsuario':nombre, 'fechaActual':fechaActual})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
    