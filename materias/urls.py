from django.urls import path
from . import views

urlpatterns = [
    path('', views.materias, name='materias' ),
    path('<int:materia_id>/', views.materia, name='materia' ),

]