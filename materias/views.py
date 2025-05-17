from django.shortcuts import render
from app.models import Materia
from app.forms import MateriaForm
from django.contrib.auth.decorators import login_required

@login_required
def materia(request, pk):
     """View de matérias individuais"""
     materia = Materia.objects.get(pk = pk)

     if materia.user != request.user:
          return render(request, 'app/erro_404.html', status=404)
     
     comentarios = materia.comentario_set.order_by('-date_added') 
     context = {'materia':materia, 'comentarios':comentarios}
     return render(request, 'materias/materia.html', context)

@login_required
def materias(request):
     """View da lista de matérias"""
     materias = Materia.objects.order_by('date_added') # apaguei isso antes de order_by: .filter(user = request.user)
     context = {'materias':materias}
     return render(request, 'materias/materias.html', context)
