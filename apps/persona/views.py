from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.forms import PersonaForm
from apps.persona.models import Persona

def saludoP(request):
    return render(request, 'persona/index.html')

def persona_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            print("guardar")
            form.save()
        return redirect('persona:index')
    else:
        form = PersonaForm()
    return render(request,'persona/indexp.html', {'form':form})

def persona_list(request):
    persona = Persona.objects.all()
    context = {
        'personas': persona
    }
    return render(request, 'persona/tables_persona.html',context)