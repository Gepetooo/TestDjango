from django.urls import path

from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar'),
    path('remover/<int:tarefa_id>/', views.remover_tarefa, name='remover'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar'),
]
