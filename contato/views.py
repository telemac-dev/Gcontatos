from django.shortcuts import render
from django.views.generic import ListView, CreateView
from contato.forms import PessoaForm
from contato.models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'
    