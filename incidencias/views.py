from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Linea, Estacion, Incidencia

# Create your views here.
class ListadoView(generic.ListView): 
    template_name = 'incidencias/listado.html'
    context_object_name = 'estaciones'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Estacion.objects.order_by('linea')
    
    
class CrearIncidenciaView(generic.DetailView): 
    template_name = 'incidencias/crearIncidencia.html'
    model = Estacion
    
    
def guardar(request, pk):
    estacion = get_object_or_404(Estacion, pk=pk)
    if request.POST['incidencia']:
        incidencia = Incidencia(texto=request.POST['incidencia'], fecha=timezone.now(), estacion=estacion)
        incidencia.save()     
        return HttpResponseRedirect(reverse('incidencias:listado'))
    else:
        return render(request, 'incidencias/crearIncidencia.html', {
            'estacion': estacion,
            'mensaje_error': "Faltan campos por rellenar"
        })

        # selected_choice.votes += 1
        # selected_choice.save()
        # # Always return an HttpResponseRedirect after successfully dealing
        # # with POST data. This prevents data from being posted twice if a
        # # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    