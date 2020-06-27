from django.db import models


class TodoList(models.Model):
    list_name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('list_name', )

    def __str__(self):
        return self.list_name


class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, related_name='todo_items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ('item_name', )
