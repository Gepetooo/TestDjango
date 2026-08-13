from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome
