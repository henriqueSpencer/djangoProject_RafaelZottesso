# from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class PaginaInicial(TemplateView):  #criando nossa primeira view
    template_name = 'index.html'
    #template_name ='modelo.html' #'paginas/modelo.html' deu erro assim

class SobreView(TemplateView):
    template_name = 'sobre.html'   #paginas/sobre.html' deu erro assim