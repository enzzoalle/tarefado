from django import forms

class LoginForm(forms.Form):

     login = forms.CharField(
          max_length=35,
          widget=forms.TextInput(attrs={
               'placeholder':'Digite o email ou o usuário',
               'id':'cadastro_user_login',
               'class':'form-control',
          })
     )

     password = forms.CharField(
          max_length=22,
          widget=forms.PasswordInput(attrs={
               'placeholder':'Digite sua senha',
               'id':'cadastro_user_password',
               'class':'form-control',
          })
     )