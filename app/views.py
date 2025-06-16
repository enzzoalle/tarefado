from django.shortcuts import render, get_object_or_404
from app.models import Tarefa, TarefaAgenda
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def index(request):
    if request.user.is_authenticated:
        hoje = timezone.now().date()
        daqui_sete_dias = hoje + timedelta(days=7)

        # Tarefas comuns
        tarefas_gerais = Tarefa.objects.filter(user=request.user, status=False).order_by('-date_added')

        # Tarefas da agenda
        tarefas_agenda = TarefaAgenda.objects.filter(user=request.user, status=False).order_by('data_entrega')

        # Tarefas com prazo dentro dos próximos 7 dias
        tarefas_proximas = TarefaAgenda.objects.filter(user=request.user, status=False, data_entrega__range=(hoje, daqui_sete_dias)).order_by('data_entrega')

        return render(request, 'app/index.html', {'tarefas_gerais': tarefas_gerais, 'tarefas_agenda': tarefas_agenda, 'tarefas_proximas': tarefas_proximas})

    return render(request, 'app/index.html')
