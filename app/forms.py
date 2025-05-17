from .models import Tarefa, Comentario, Materia
from django import forms

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['titulo']
        label = {'titulo':''}

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']
        label = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'cols':50})}

class TarefaForm(forms.Form):
    tarefa = forms.CharField(
        max_length=55,
        required = True,
        widget = forms.TextInput(
            attrs={
                'id':'id_tarefa',
                'class':'form-control',
                'placeholder':'Digite sua tarefa...'}))
