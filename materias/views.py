from django.shortcuts import render
from app.models import Materia
from django.contrib.auth.decorators import login_required
from app.forms import MateriaForm
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def materia(request, materia_id):
    """Página de matéria única"""
    materia = Materia.objects.get(id = materia_id)

    # garante que a matéria pertença ao usuário atual
    if materia.user != request.user:
        return render(request, 'app/erro_404.html', status=404)
    
    comentarios = materia.comentario_set.order_by('-date_added')
    context = {'materia': materia, 'comentarios': comentarios}
    return render(request, 'materias/materia.html', context)

@login_required
def materias(request):
    """Página que lista todas as matérias"""
    materias = Materia.objects.filter(user=request.user).order_by('date_added')
    context = {'materias': materias}
    return render(request, 'materias/materias.html', context)

@login_required
def nova_materia(request):
    """Para adicionar uma nova matéria"""
    if request.method != 'POST':
        # nenhuma matéria submetida, cria um formulário em branco
        form = MateriaForm()
    else: 
        form = MateriaForm(request.POST)
        if form.is_valid():
            nova_materia = form.save(commit=False)
            nova_materia.user = request.user
            nova_materia.save()
            return HttpResponseRedirect(reverse('materias'))
        
    context = {'form':form}
    return render(request, 'materias/nova_materia.html', context)

@login_required
def excluir_materia(request, materia_id):
    materia = Materia.objects.get(id=materia_id)

    # garante que a matéria pertença ao usuário atual
    if materia.user != request.user:
        return render(request, 'app/erro_404.html', status=404)
    if request.method == 'POST':
        materia.delete()
        return HttpResponseRedirect(reverse('materias'))
    
    context = {'materia':materia}
    return render (request, 'materias/excluir_matéria.html', context)