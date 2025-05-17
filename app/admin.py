from django.contrib import admin
from .models import Tarefa, Comentario, Materia

admin.site.register(Tarefa)
admin.site.register(Materia)
admin.site.register(Comentario)