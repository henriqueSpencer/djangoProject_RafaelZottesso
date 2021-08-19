from django.urls import path
from .views import PaginaInicial, SobreView #eese ponto é para dizer q esta pegando algo nesse diretorio paginas

urlpatterns = [
#    #path('endereço/', IndexView.as_view(), name='nome-da-url'),
    path('', PaginaInicial.as_view(), name='index'),        #'inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]