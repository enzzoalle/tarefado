from django.shortcuts import render, redirect, get_object_or_404
from app.models import Materia, Comentario
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from app.forms import MateriaForm, ComentarioForm

@login_required(login_url='login_view')
def materia(request, materia_id):
    """Exibe uma matéria específica e seus comentários"""
    materia = get_object_or_404(Materia, id=materia_id, user=request.user)
    comentarios = materia.comentario_set.order_by('-date_added')

    context = {'materia': materia, 'comentarios': comentarios}
    return render(request, 'materias/materia.html', context)

@login_required(login_url='login_view')
def materias(request):
    """Lista todas as matérias do usuário"""
    materias = Materia.objects.filter(user=request.user).order_by('date_added')
    context = {'materias': materias}
    return render(request, 'materias/materias.html', context)

@login_required(login_url='login_view')
def nova_materia(request):
    """Cria uma nova matéria"""
    form = MateriaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        nova = form.save(commit=False)
        nova.user = request.user
        nova.save()
        return redirect('materias')

    context = {'form': form}
    return render(request, 'materias/nova_materia.html', context)

@login_required(login_url='login_view')
@require_POST
def excluir_materia(request, materia_id):
    """Exclui uma matéria"""
    materia = get_object_or_404(Materia, id=materia_id, user=request.user)
    materia.delete()
    return redirect('materias')

@login_required(login_url='login_view')
def novo_comentario(request, materia_id):
    """Adiciona um novo comentário à matéria"""
    materia = get_object_or_404(Materia, id=materia_id, user=request.user)
    form = ComentarioForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comentario = form.save(commit=False)
        comentario.materia = materia
        comentario.save()
        return redirect('materia', materia_id=materia.id)

    context = {'materia': materia, 'form': form}
    return render(request, 'materias/novo_comentario.html', context)

@login_required(login_url='login_view')
def editar_comentario(request, comentario_id):
    """Edita um comentário existente"""
    comentario = get_object_or_404(Comentario, id=comentario_id, materia__user=request.user)
    form = ComentarioForm(request.POST or None, instance=comentario)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('materia', materia_id=comentario.materia.id)

    context = {'comentario': comentario, 'materia': comentario.materia,'form': form}
    return render(request, 'materias/editar_comentario.html', context)

@login_required(login_url='login_view')
@require_POST
def excluir_comentario(request, comentario_id):
    """Exclui um comentário"""
    comentario = get_object_or_404(Comentario, id=comentario_id, materia__user=request.user)
    materia_id = comentario.materia.id
    comentario.delete()
    return redirect('materia', materia_id=materia_id)