from django.shortcuts import render, redirect, get_object_or_404
from app.models import Tarefa
from app.forms import TarefaForm
from django.contrib.auth.decorators import login_required

@login_required
def tarefas(request):
    """Página de tarefas"""
    tarefas_pendentes = Tarefa.objects.filter(user=request.user, status=False)
    tarefas_concluidas = Tarefa.objects.filter(user=request.user, status=True)

    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            nova_tarefa = form.save(commit=False)
            nova_tarefa.user = request.user
            nova_tarefa.status = False
            nova_tarefa.save()
            return redirect('tarefas')
    else:
        form = TarefaForm()

    context = {'form': form, 'tarefas_concluidas': tarefas_concluidas, 'tarefas_pendentes': tarefas_pendentes}
    return render(request, 'tarefas/tarefas.html', context)

@login_required
def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.status = True
    tarefa.save()
    return redirect('tarefas')

@login_required
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('tarefas')

@login_required
def limpar_tarefas_concluidas(request):
    Tarefa.objects.filter(user=request.user, status=True).delete()
    return redirect('tarefas')
