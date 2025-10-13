from django.db import models

class Receitas(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    instrucoes = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.titulo
