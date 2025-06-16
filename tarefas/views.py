from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models import Tarefa
from app.forms import TarefaForm

@login_required(login_url='login_view')
def tarefas(request):
    """Página de tarefas"""
    pendentes = Tarefa.objects.filter(user=request.user, status=False)
    concluidas = Tarefa.objects.filter(user=request.user, status=True)

    form = TarefaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        tarefa = form.save(commit=False)
        tarefa.user = request.user
        tarefa.status = False
        tarefa.save()
        return redirect('tarefas')

    context = {'form': form, 'tarefas_pendentes': pendentes, 'tarefas_concluidas': concluidas}
    return render(request, 'tarefas/tarefas.html', context)

@login_required(login_url='login_view')
def concluir_tarefa(request, id):
    """Marca uma tarefa como concluída"""
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    tarefa.status = True
    tarefa.save()
    return redirect('tarefas')

@login_required(login_url='login_view')
def excluir_tarefa(request, id):
    """Exclui uma tarefa"""
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    tarefa.delete()
    return redirect('tarefas')

@login_required(login_url='login_view')
def limpar_tarefas_concluidas(request):
    """Remove todas as tarefas que já foram concluídas"""
    Tarefa.objects.filter(user=request.user, status=True).delete()
    return redirect('tarefas')