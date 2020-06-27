from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoList
from .serializers import TodoListSerializer, TodoItemSerializer


class TodoListAPIView(APIView):
    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            serializer = TodoListSerializer(instance=instance)
        return Response(serializer.data)


class TodoListDetailAPIView(RetrieveAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.prefetch_related('todo_items')
