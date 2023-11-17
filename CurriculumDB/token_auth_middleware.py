from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class TokenAuthMiddleware:
  def __init__(self, get_response):
      self.get_response = get_response

  def __call__(self, request):
      auth_header = request.META.get('HTTP_AUTHORIZATION', '').split()
      if len(auth_header) == 2 and auth_header[0].lower() == 'token':
          token_key = auth_header[1]
          try:
              token = Token.objects.get(key=token_key)
              request.user = token.user
          except Token.DoesNotExist:
              pass
      return self.get_response(request)
