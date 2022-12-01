from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.vehiculo.forms import VehiculoForm
from apps.vehiculo.models import Vehiculo

def saludoV(request):
    return render(request, 'vehiculo/index.html')

def vehiculo_view(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            print("guardar")
            form.save()
        return redirect('vehiculo:index')
    else:
        form = VehiculoForm()
    return render(request,'vehiculo/indexv.html', {'form':form})

def vehiculo_list(request):
    vehiculo = Vehiculo.objects.all()
    context = {
        'vehiculo': vehiculo
    }
    return render(request, 'vehiculo/tables_vehiculo.html',context)