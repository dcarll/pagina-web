from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    '''View para a pagina inicial index'''
    template_name = 'index.html'
