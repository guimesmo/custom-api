from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404
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


class TodoListRetrieveAPIView(APIView):
    def get(self, request, pk):
        todo_list = get_object_or_404(TodoList, pk=pk)
        serializer = TodoListSerializer(instance=todo_list)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo_list = get_object_or_404(TodoList, pk=pk)
        todo_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        todo_list = get_object_or_404(TodoList, pk=pk)
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save(todo_list=todo_list)
            serializer = TodoItemSerializer(instance=instance)
        return Response(serializer.data)


class TodoListAPIView(RetrieveAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.prefetch_related('todo_items')
