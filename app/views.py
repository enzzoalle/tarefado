from django.shortcuts import render
from app.models import Tarefa, TarefaAgenda
from django.utils import timezone
from datetime import timedelta

def index(request):
    if request.user.is_authenticated:
        hoje = timezone.now().date()
        daqui_dez_dias = hoje + timedelta(days=10)

        # Tarefas comuns
        tarefas_gerais = Tarefa.objects.filter(user=request.user, status=False).order_by('-date_added')

        # Tarefas da agenda
        tarefas_agenda = TarefaAgenda.objects.filter(user=request.user, status=False).order_by('data_entrega')

        # Tarefas com prazo dentro dos próximos 10 dias
        tarefas_proximas = TarefaAgenda.objects.filter(user=request.user, status=False, data_entrega__range=(hoje, daqui_dez_dias)).order_by('data_entrega')

        return render(request, 'app/index.html', {'tarefas_gerais': tarefas_gerais, 'tarefas_agenda': tarefas_agenda, 'tarefas_proximas': tarefas_proximas})

    return render(request, 'app/index.html')
