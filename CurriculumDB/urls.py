from django.urls import path, include

urlpatterns = [
    path('user/', include('User.urls')),
    path('curriculumvitae/', include('CurriculumVitae.urls')),
    path('auth/', include('rest_authtoken.urls')),
]
