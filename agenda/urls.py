from django.urls import path
from . import views

urlpatterns = [
     path('', views.agenda, name='agenda'),
    path('concluir_tarefa_agenda/<int:id>', views.concluir_tarefa_agenda, name='concluir_tarefa_agenda'),
    path('excluir_tarefa_agenda/<int:id>', views.excluir_tarefa_agenda, name='excluir_tarefa_agenda'),
    path('limpar_tarefas_agenda/', views.limpar_tarefas_concluidas_agenda, name='limpar_tarefas_concluidas_agenda')
]