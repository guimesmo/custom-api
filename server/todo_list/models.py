from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList)
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
