from  django.http import HttpResponse

def saludo(request):
    list_numeros = [ int(num) for num in request.GET['numeros'].split(',')]
    print(list_numeros)
    return HttpResponse(str(sorted(list_numeros)))

def mayor_edad(request, nombre, edad):
    if edad >=18:
        mensaje = f'hola {nombre} puedes ingresar'
    else:
        mensaje = f'hola {nombre} no puedes ingresar {edad}'
    return HttpResponse(mensaje)