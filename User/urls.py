from django.urls import path
from .views import LoginView, RegisterView, UserView #, ValidateTokenView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserView.as_view(), name='user-list'),
 #  path('validate_token/', ValidateTokenView.as_view(), name='validate_token'),
]
