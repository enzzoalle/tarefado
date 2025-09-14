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
        return f"[{self.materia}] {self.text[:50]}..."
     
class ArquivoComentario(models.Model):
    comentario = models.ForeignKey('Comentario', on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(upload_to='comentarios/arquivos/')

    def __str__(self):
        return f"[{self.comentario.materia}] Comentário: {self.comentario.text[:40]}..."
     
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
        materia_nome = self.materia.titulo if self.materia else "Sem matéria"
        data = self.data_entrega.strftime('%d/%m/%Y') if self.data_entrega else "Sem data"
        return f"{self.tarefa} | {materia_nome} | {data}"

class Prompt(models.Model):
    TEMPLATE_CHOICES = [
        ("conceito", "Conceito a Fundo"),
        ("projeto", "Projeto Real"),
        ("revisao", "Revisão"),
        ("skill", "Aprendizado por Skill"),
        ("profissional", "Desenvolvimento Profissional"),
        ("escrita", "Escrita Técnica"),
        ("checklist", "Checklist Técnico"),
        ("simulacao", "Simulação de Projeto"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prompts")
    titulo = models.CharField(max_length=120)
    conteudo = models.TextField()
    template_key = models.CharField(max_length=30, choices=TEMPLATE_CHOICES, blank=True, null=True)
    # Mantém colunas antigas sem renomear no banco
    date_added = models.DateTimeField(auto_now_add=True, db_column="criado_em")
    date_updated = models.DateTimeField(auto_now=True, db_column="atualizado_em")

    class Meta:
        db_table = "app_prompt"
        ordering = ["-date_updated"]

    def __str__(self):
        return self.titulo