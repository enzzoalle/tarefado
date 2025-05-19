from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

def login_view(request):

     if request.user.is_authenticated:
          return redirect('index')
          
     if request.method == 'POST':
          form = LoginForm(request.POST)

          if form.is_valid():
               user_login = form.cleaned_data['login']
               password = form.cleaned_data['password']

               user = User.objects.filter(Q(username=user_login) | Q(email=user_login)).first() # para procurar por username ou email no campo de login

               if user is not None: # para ter certeza que o usuario existe
                    username = user.username
                    authenticate_user = authenticate(request, username=username, password=password)

                    if authenticate_user is not None:
                         login(request, authenticate_user)
                         return redirect('index')

                    else:
                         form.add_error('login', 'Login inválido ou inexistente!')
                         context = {'form':form}
                         return render(request, 'authenticate/login.html', context)
                    
               else:
                    form.add_error('login', 'Login inválido ou inexistente!')
                    context = {'form':form}
                    return render(request, 'authenticate/login.html', context)

          else:
               context = {'form':form}
               return render(request, 'authenticate/login.html', context)

     form = LoginForm()
     context = {'form':form}
     return render(request, 'authenticate/login.html', context)

def logout_view(request):
     if request.user.is_authenticated:
          logout(request)
          return redirect('index')
     
     else:
          return redirect('index')
