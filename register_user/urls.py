from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('register_user', views.register_user, name='register_user'),
    path('confirmar_email/<str:code>', views.confirmar_email, name='confirmar_email'),
    path('codigo_expirado', views.codigo_expirado, name='codigo_expirado'),
    path('email_sucesso', views.email_sucesso, name='email_sucesso'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='register_user/password_reset/reset_password.html', form_class=MyPasswordResetForm) , name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='register_user/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='register_user/password_reset/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='register_user/password_reset/password_reset_complete.html'), name='password_reset_complete'),
]
