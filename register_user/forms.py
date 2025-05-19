from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class RegisterForm(UserCreationForm):
     username = forms.CharField(
          max_length=15,
          required=True,
          widget=forms.TextInput(attrs={
               'class':'form-control',
               'id':'cadastro_user_username',
          })
     )

     email = forms.EmailField(
          max_length=35,
          required=True,
          widget=forms.EmailInput(attrs={
               'class':'form-control',
               'id':'cadastro_user_email',
               'aria-describedby':'emailHelp',
          })
     )

     password1 = forms.CharField(
          max_length=22,
          required=True,
          widget=forms.PasswordInput(attrs={
               'class':'form-control',
               'id':'cadastro_user_password1',
          })
     )

     password2 = forms.CharField(
          max_length=22,
          required=True,
          widget=forms.PasswordInput(attrs={
               'class':'form-control',
               'id':'cadastro_user_password2',
          })
     )

     class Meta:
          model = User
          fields = ['username', 'email', 'password1', 'password2']

class MyPasswordResetForm(PasswordResetForm):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

          self.fields['email'].widget.attrs.update({
               'class':'form-control',
               'placeholder':'Digite seu email:',
          })

class MySetPasswordForm(SetPasswordForm):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

          self.fields['new_password1'].widget.attrs.update({
               'class':'form-control',
               'placeholder':'Digite sua nova senha:',
          })

          self.fields['new_password2'].widget.attrs.update({
               'class':'form-control',
               'placeholder':'Confirme sua nova senha:',
          })