from django.shortcuts import render
from .models import Tarefa
from .forms import TarefaForm

def index(request):
     return render(request, 'app/index.html')