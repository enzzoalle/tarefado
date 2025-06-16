from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('materias/', include('materias.urls')),
    path('register/', include('register_user.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('tarefas/', include('tarefas.urls')),
    path('agenda/', include('agenda.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
