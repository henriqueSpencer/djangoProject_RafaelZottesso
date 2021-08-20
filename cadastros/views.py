#from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade, Status, Classe, Campus

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')#vai dizer a url q sera direcionando caso der tudo certo

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClasseCreate(CreateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CampusCreate(CreateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

################### UPDATE ############################

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')  # vai dizer a url q sera direcionando caso der tudo certo

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class StatusUpdate(UpdateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClasseUpdate(UpdateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CampusUpdate(UpdateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

################### DELETE ############################

class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')  # vai dizer a url q sera direcionando caso der tudo certo

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class StatusDelete(DeleteView):
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class ClasseDelete(DeleteView):
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class CampusDelete(DeleteView):
    model = Campus
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

################### LISTA ############################

class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class AtividadeList(LoginRequiredMixin, ListView): #TODO:login serve para ficar acessivel so se logado
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

class StatusList(ListView):
    model = Status
    template_name = 'cadastros/listas/status.html'

class ClasseList(ListView):
    model = Classe
    template_name = 'cadastros/listas/classe.html'

class CampusList(ListView):
    model = Campus
    template_name = 'cadastros/listas/campus.html'
