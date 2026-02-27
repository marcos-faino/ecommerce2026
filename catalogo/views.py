from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Produto


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont["prods"] = Produto.disponiveis.all().order_by("?")[:3]
        return cont