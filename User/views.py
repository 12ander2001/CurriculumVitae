from django.http import JsonResponse
from django.views import View
from User.models import CustomUser
from rest_framework.views import APIView

class UserListView(View):
    def get(self, request):
        users = CustomUser.objects.all().values()
        return JsonResponse(list(users), safe=False)

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .models import CustomUser
from rest_framework.authtoken.models import Token


class LoginView(APIView):
  def post(self, request):
      email = request.data.get('email')
      password = request.data.get('password')

      user = authenticate(request, username=email, password=password)

      if user is not None:
          token, created = Token.objects.get_or_create(user=user)
          return Response({'user_id': user.id, 'token': token.key})
      else:
          return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        firstname = request.data.get('firstname')
        lastname = request.data.get('lastname')

        if not email or not password or not username or not firstname or not lastname:
            return Response({'error': 'Todos los campos son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.create_user(email=email, password=password, username=username, firstname=firstname, lastname=lastname)
            return Response({'message': 'Usuario registrado exitosamente'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
