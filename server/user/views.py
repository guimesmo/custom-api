from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            instance.set_password(serializer.validated_data.get('password'))
            instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
