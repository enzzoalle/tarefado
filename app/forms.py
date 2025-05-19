from .models import Tarefa, Comentario, Materia
from django import forms

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['titulo']
        labels = {'titulo': ''}
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class':'form-control',
                'id':'nova_materia'
            })
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'cols':55})}

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['tarefa']
        labels = {'tarefa': ''}
        widgets = {
            'tarefa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua nova tarefa...'})}