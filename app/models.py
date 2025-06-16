from django.db import models
from django.contrib.auth.models import User

class Materia(models.Model):
     titulo = models.CharField(max_length=55)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     date_added = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.titulo
     
class Comentario(models.Model):
     materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
     text = models.TextField()
     date_added = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.text[:50] + "..."
     
class Tarefa(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     tarefa = models.CharField(max_length=55)
     status = models.BooleanField(default=False)
     date_added = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return self.tarefa
     
class TarefaAgenda(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     tarefa = models.CharField(max_length=55)
     status = models.BooleanField(default=False)
     materia = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True, blank=True)
     data_entrega = models.DateField(null=True, blank=True)
     
     def __str__(self):
          return self.tarefa