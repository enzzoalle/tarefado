from django.urls import path
from . import views

urlpatterns = [
     path('', views.tarefas, name='tarefas' ),
    path('concluir_tarefa/<int:id>', views.concluir_tarefa, name='concluir_tarefa'),
    path('excluir_tarefa/<int:id>', views.excluir_tarefa, name='excluir_tarefa'),
    path('limpar_tarefas/', views.limpar_tarefas_concluidas, name='limpar_tarefas_concluidas')
]