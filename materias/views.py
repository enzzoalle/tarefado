from django.shortcuts import render
from app.models import Materia
from django.contrib.auth.decorators import login_required

@login_required # exige login do usuário para acessar esta aba, no caso as materias
def materia(request, materia_id):
    """Página de matéria única"""
    materia = Materia.objects.get(id = materia_id)

    # garante que a matéria pertença ao usuário atual
    if materia.user != request.user:
        return render(request, 'app/erro_404.html', status=404)
    
    comentarios = materia.comentario_set.order_by('-date_added') # o "-" é para começar da ordem inversa
    context = {'materia': materia, 'comentarios': comentarios}
    return render(request, 'materias/materia.html', context)

@login_required # exige login do usuário para acessar esta aba, no caso as materias
def materias(request):
    """Página que lista todas as matérias"""
    materias = Materia.objects.filter(user=request.user).order_by('date_added')
    context = {'materias': materias}
    return render(request, 'materias/materias.html', context)
