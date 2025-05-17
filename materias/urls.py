from django.urls import path
from . import views

urlpatterns = [
    path('', views.materias, name='materias' ),
    path('<int:pk>/', views.materia, name='materia' ),

]