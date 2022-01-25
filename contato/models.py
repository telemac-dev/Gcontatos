from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True)
    ativo = models.BooleanField(default=True)

