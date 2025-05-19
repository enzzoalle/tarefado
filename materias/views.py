from django.shortcuts import render
from app.models import Materia, Comentario
from django.contrib.auth.decorators import login_required
from app.forms import MateriaForm, ComentarioForm
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
    return render (request, 'materias/excluir_materia.html', context)

@login_required
def novo_comentario(request, materia_id):
    materia = Materia.objects.get(id=materia_id)

    if materia.user != request.user:
        return render(request, 'app/erro_404.html', status=404)
    
    if request.method != 'POST':
        form = ComentarioForm()
    else:
        form = ComentarioForm(data=request.POST)

        if form.is_valid():
            novo_comentario = form.save(commit=False)
            novo_comentario.materia = materia
            novo_comentario.save()
            return HttpResponseRedirect(reverse('materia', args=[materia_id]))
        
    context = {'materia': materia, 'form':form}
    return render(request, 'materias/novo_comentario.html', context)

@login_required
def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    materia = comentario.materia

    if materia.user != request.user:
        return render(request, 'app/erro_404.html', status=404)
    
    if request.method != 'POST':
        form = ComentarioForm(instance=comentario)
    else:
        form = ComentarioForm(instance=comentario, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('materia', args=[materia.id]))
        
    context = {'comentario': comentario, 'materia': materia, 'form':form}
    return render(request, 'materias/editar_comentario.html', context)

@login_required
def excluir_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    materia = comentario.materia

    if materia.user != request.user:
        return render(request, 'app/erro_404.html', status=404)
    
    if request.method == 'POST':
        comentario.delete()
        return HttpResponseRedirect(reverse('materia', args=[materia.id]))
    
    context = {'comentario':comentario, 'materia':materia}
    return render (request, 'materias/excluir_comentario.html', context)