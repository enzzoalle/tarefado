from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from . import enviar_email
from .models import CodigoEmail
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone

def register_user(request):

     if request.user.is_authenticated:
          return redirect('index')

     if request.method == 'POST':
          form = RegisterForm(request.POST)

          if form.is_valid():

               email = form.cleaned_data['email']
               dominio = request.get_host()

               user = form.save(commit=False) # pro usuário ser salvo inativo
               user.is_active = False
               user.save()

               code = CodigoEmail.objects.create(user=user)
               code.save()

               url = 'http://'+ dominio + '/register/confirmar_email/' + code.code
               enviar_email.enviar_email(url=url, email=email)

               messages.success(request, 'Usuário registrado com sucesso, verifique seu email em até 5 minutos para confirmação de cadastro. (Verifique o lixo eletrônico e spam)')
               return redirect('register_user')

          else:
               context = {'form':form}
               return render(request, 'register_user/register_user.html', context)

     form = RegisterForm()
     context = {'form':form}
     return render(request, 'register_user/register_user.html', context)

def confirmar_email(code):
     codigo_email = get_object_or_404(CodigoEmail, code=code)
     user = codigo_email.user

     data_hora_codigo = codigo_email.data_code
     validade = data_hora_codigo + timedelta(minutes=5) # 5 minuto a partir da hora da criação
     data_hora_agora = timezone.now()

     if data_hora_agora > validade:
          user.delete()
          return redirect('codigo_expirado')
     
     else:
          user.is_active = True
          user.save()
          codigo_email.delete() # para deletar o codigo do banco de dados assim que o user for ativo

          return redirect('email_sucesso')

def codigo_expirado(request):
     return render(request, 'register_user/codigo_expirado.html')

def email_sucesso(request):
     return render(request, 'register_user/email_sucesso.html')