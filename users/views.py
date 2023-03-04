import uuid
import random

from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device

class RegisterView(APIView):

    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user, created = User.objects.get_or_create(email=email)

        if not created:
            return Response({"detail":"User already created"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        device = Device.objects.create(user=user)

        code = random.randint(10000, 99999)

        # send message email
        # ? should how to setup cache memory for send code learned
        cache.set(str(email), code, 2 * 60)
        return Response({"code":code})
    
class GetTokenView(APIView):
    
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")

        cached_code = cache.get(str(email))

        if code != cached_code:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        token = str(uuid.uuid4())

        return Response({"token":token})
    