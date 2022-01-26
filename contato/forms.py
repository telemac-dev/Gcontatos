from django.forms import models, fields
from .models import Pessoa


class PessoaForm(models.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativo']

