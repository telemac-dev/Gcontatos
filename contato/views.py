from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from contato.forms import PessoaForm
from contato.models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')

    # Filtro de busca
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None
        filtro_ativo = self.request.GET.get('ativo') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)

        if filtro_ativo:
            queryset = queryset.filter(ativo__contains=filtro_ativo)

        return queryset


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'
