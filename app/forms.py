from .models import Tarefa, Comentario, Materia, TarefaAgenda, Prompt
from django import forms

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['titulo']
        labels = {'titulo': ''}
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class':'form-control',
                'id':'nova_materia'})}

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['tarefa']
        labels = {'tarefa': ''}
        widgets = {
            'tarefa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua nova tarefa...'})}
        
class TarefaAgendaForm(forms.ModelForm):
    class Meta:
        model = TarefaAgenda
        fields = ['tarefa', 'data_entrega', 'materia']
        widgets = {
            'tarefa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua nova tarefa...'
            }),
            'data_entrega': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Defina a data de entrega...'
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['materia'].queryset = Materia.objects.filter(user=user).order_by('titulo')
            self.fields['materia'].required = False
            self.fields['materia'].empty_label = 'Sem matéria vinculada'

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["titulo", "template_key", "conteudo"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título"}),
            "template_key": forms.Select(attrs={"class": "form-select", "id": "templateSelect"}),
            "conteudo": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Conteúdo do prompt"}),
        }