from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from todo_list.views import TodoListAPIView, TodoListRetrieveAPIView, TodoListItemAPIView
from user.views import UserView

urlpatterns = [
    path('login', obtain_auth_token),
    path('register', UserView.as_view()),
    path('list', TodoListAPIView.as_view()),
    path('list/<int:pk>', TodoListRetrieveAPIView.as_view()),
    path('list/<int:list_id>/<int:pk>', TodoListItemAPIView.as_view()),
]
