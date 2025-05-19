from django.shortcuts import render

def index(request):
     return render(request, 'app/index.html')

def erro_404(request):
    """View personalizada para erros 404."""
    return render(request, 'app/erro_404.html', status=404)