from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from pshop.models import Cliente, Pet, Servico


def index(requet):
    return render(requet, 'pshop/layouts/index.html')


class ClientesList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('pshop:list_cliente')


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('pshop:list_cliente')


class ClienteDelete(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('pshop:list_cliente')


class PetList(ListView):
    model = Pet
    queryset = Pet.objects.all()


class PetCreate(CreateView):
    model = Pet
    fields = '__all__'
    success_url = reverse_lazy('pshop:list_pet')


class PetCreate(CreateView):
    model = Pet
    fields = '__all__'
    success_url = reverse_lazy('pshop:list_pet')


class PetUpdate(UpdateView):
    model = Pet
    fields = '__all__'
    success_url = reverse_lazy('pshop:list_pet')


class PetDelete(DeleteView):
    queryset = Pet.objects.all()
    success_url = reverse_lazy('pshop:list_pet')


class ServicoList(ListView):
    model = Servico
    queryset = Servico.objects.all()


class ServicoCreate(CreateView):
    model = Servico
    fields = '__all__'
    success_url = reverse_lazy('pshop:list_servico')


class ServicoUpdate(UpdateView):
    model = Servico
    fields = '__all__'
    success_url = reverse_lazy('pshop:list_servico')


class ServicoDelete(DeleteView):
    queryset = Servico.objects.all()
    success_url = reverse_lazy('pshop:list_servico')


def about(requet):
    return render(requet, 'pshop/layouts/about.html')