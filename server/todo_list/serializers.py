from rest_framework import serializers

from .models import TodoList, TodoItem


class TodoItemSerializer(serializers.Serializer):
    todo_item_id = serializers.IntegerField(source='id')
    todo_item_name = serializers.CharField(source='item_name')

    class Meta:
        model = TodoItem
        fields = ('', 'name', )


class TodoListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    todo_items = TodoItemSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'list_name', 'todo_items', )
