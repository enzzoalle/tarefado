from django.urls import path
from . import views

urlpatterns = [
    path('', views.materias, name='materias' ),
    path('<int:materia_id>/', views.materia, name='materia' ),
    path('<int:materia_id>/excluir', views.excluir_materia, name='excluir_materia'),
    path('nova_materia/', views.nova_materia, name='nova_materia'),
]