from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('materias/', include('materias.urls')),
    path('register/', include('register_user.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('tarefas/', include('tarefas.urls')),
]
