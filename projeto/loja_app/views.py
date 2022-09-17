from loja_app.models import Marca, Produto
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'loja_app/base.html'

class ListMarcaView(ListView):
    model = Marca
    template_name = 'loja_app/marca/marca_list.html'

class CreateMarcaView(CreateView):
    model = Marca
    fields = '__all__'
    template_name = 'loja_app/marca/marca_form.html'
    success_url = reverse_lazy('loja_app:list-marca')


class ListProdutoView(ListView):
    model = Produto
    template_name = 'loja_app/produto/produto_list.html'

class CreateProdutoView(CreateView):
    model = Produto
    fields = '__all__'
    template_name = 'loja_app/produto/produto_form.html'
    success_url = reverse_lazy('loja_app:list-produto')

class DetailProdutoView(DetailView):
    model = Produto
    template_name = 'loja_app/produto/produto_detail.html'


class DeleteProdutoView(DeleteView):
    model = Produto
    success_url = reverse_lazy('loja_app:list-produto')
    template_name = 'loja_app/produto/produto_confirm_delete.html'

class UpdateProdutoView(UpdateView):
    model = Produto
    fields = '__all__'
    template_name = 'loja_app/produto/produto_form.html'