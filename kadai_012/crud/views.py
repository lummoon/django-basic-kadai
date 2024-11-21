from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# 「【課題】商品詳細画面を作成しよう」で追加
from django.views.generic.detail import DetailView

from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

# 「【課題】商品詳細画面を作成しよう」で追加
class ProductDetailView(DetailView):
    model = Product