from django.contrib import admin
from .models import Tarefa, Comentario, Materia, TarefaAgenda, ArquivoComentario

admin.site.register(Tarefa)
admin.site.register(Materia)
admin.site.register(Comentario)
admin.site.register(TarefaAgenda)
admin.site.register(ArquivoComentario)