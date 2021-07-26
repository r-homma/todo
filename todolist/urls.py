from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todoAdd', views.todoAdd, name='todoAdd'),
    path('todoDelete/<int:del_id>', views.todoDelete, name='todoDelete'),# todoDelete/<int:del_id>によって削除したいToDoを指定することができる
    path('todoEdit/<int:edit_id>', views.todoEdit, name='todoEdit'),
]