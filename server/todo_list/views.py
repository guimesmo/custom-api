from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TodoListSerializer, TodoItemSerializer


class UserView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        serializer = TodoListSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            serializer = TodoListSerializer(instance=instance)
        return Response(serializer.data)

