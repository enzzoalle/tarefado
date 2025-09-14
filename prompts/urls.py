from django.urls import path
from . import views

urlpatterns = [
    path("", views.prompts, name="prompts"),
    path("<int:pk>/editar/", views.prompt_edit, name="prompt_edit"),
    path("<int:pk>/excluir/", views.prompt_delete, name="prompt_delete"),
]