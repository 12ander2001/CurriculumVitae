from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Esta línea habilita el panel de administración
    path('user/', include('User.urls')),
    path('curriculumvitae/', include('CurriculumVitae.urls')),
    path('auth/', include('rest_authtoken.urls')),
]
