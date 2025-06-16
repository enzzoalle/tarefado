from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models import TarefaAgenda
from app.forms import TarefaAgendaForm

@login_required(login_url='login_view')
def agenda(request):
    """Página principal da Agenda (tarefas com prazo)"""
    pendentes = TarefaAgenda.objects.filter(user=request.user, status=False).order_by('data_entrega')
    concluidas = TarefaAgenda.objects.filter(user=request.user, status=True).order_by('-data_entrega')

    form = TarefaAgendaForm(request.POST or None, user=request.user)

    if request.method == 'POST' and form.is_valid():
        tarefa = form.save(commit=False)
        tarefa.user = request.user
        tarefa.status = False
        tarefa.save()
        return redirect('agenda')

    context = {
        'form': form,
        'tarefas_pendentes': pendentes,
        'tarefas_concluidas': concluidas,
    }
    return render(request, 'agenda/agenda.html', context)

@login_required(login_url='login_view')
def concluir_tarefa_agenda(request, id):
    """Marca uma tarefa da agenda como concluída"""
    tarefa = get_object_or_404(TarefaAgenda, id=id, user=request.user)
    tarefa.status = True
    tarefa.save()
    return redirect('agenda')

@login_required(login_url='login_view')
def excluir_tarefa_agenda(request, id):
    """Exclui uma tarefa da agenda"""
    tarefa = get_object_or_404(TarefaAgenda, id=id, user=request.user)
    tarefa.delete()
    return redirect('agenda')

@login_required(login_url='login_view')
def limpar_tarefas_concluidas_agenda(request):
    """Remove todas as tarefas da agenda que já foram concluídas"""
    TarefaAgenda.objects.filter(user=request.user, status=True).delete()
    return redirect('agenda')