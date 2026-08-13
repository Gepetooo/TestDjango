from django.shortcuts import redirect, render
from .forms import TarefaForm
from django.http import HttpRequest
from django.utils import timezone
from .models import Tarefa

def home(request):
    context = {
        "nome": "Gepeto",
        "tarefas": Tarefa.objects.all(),
    }
    return render(request, 'tarefas/home.html', context)

def adicionar_tarefa(request: HttpRequest):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas:home')
    context = {
        "form": TarefaForm(),
        "success": False,
    }
    return render(request, 'tarefas/tasks.html', context)

def remover_tarefa(request: HttpRequest, tarefa_id: int):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas:home')
    context = {
        "tarefa": tarefa,
    }
    return render(request, 'tarefas/confirmar_remocao.html', context)

def editar_tarefa(request: HttpRequest, tarefa_id: int):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if request.method == 'POST':
        valores_originais = {
            'nome': tarefa.nome,
            'descricao': tarefa.descricao,
            'concluida': tarefa.concluida,
        }
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            houve_mudanca = any(
                form.cleaned_data.get(campo) != valor
                for campo, valor in valores_originais.items()
            )
            if houve_mudanca:
                tarefa.data_edicao = timezone.now()
            form.save()
            return redirect('tarefas:home')
    else:
        form = TarefaForm(instance=tarefa)
    context = {
        "form": form,
        "tarefa": tarefa,
    }
    return render(request, 'tarefas/editar_tarefa.html', context)