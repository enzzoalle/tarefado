from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_view')
def prompts(request):
     return render(request, 'prompts/prompts.html')
