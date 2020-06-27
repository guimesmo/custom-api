from rest_framework.generics import CreateAPIView, RetrieveAPIView


from .models import TodoList
from .serializers import TodoListSerializer, TodoItemSerializer


class TodoListCreateAPIView(CreateAPIView):
    serializer_class = TodoListSerializer


class TodoListDetailAPIView(RetrieveAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.prefetch_related('todo_items')
