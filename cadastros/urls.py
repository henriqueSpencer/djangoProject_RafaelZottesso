from django.urls import path

from .views import CampoCreate, AtividadeCreate, StatusCreate, CampusCreate, ClasseCreate
from .views import CampoUpdate, AtividadeUpdate, StatusUpdate, CampusUpdate, ClasseUpdate
from .views import CampoDelete, AtividadeDelete, StatusDelete, CampusDelete, ClasseDelete
from .views import CampusList, AtividadeList, StatusList, CampoList, ClasseList

urlpatterns = [
#    #path('endereço/', IndexView.as_view(), name='nome-da-url'),
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),
    path('cadastrar/campus/', CampusCreate.as_view(), name="cadastrar-campus"),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"), #int pk = primari key
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name="editar-atividade"),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name="editar-status"),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name="editar-classe"),
    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name="editar-campus"),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name="excluir-campo"),  # int pk = primari key
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade"),  # int pk = primari key
    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name="excluir-status"),  # int pk = primari key
    path('excluir/classe/<int:pk>/', ClasseDelete.as_view(), name="excluir-classe"),  # int pk = primari key
    path('excluir/campus/<int:pk>/', CampusDelete.as_view(), name="excluir-campus"),  # int pk = primari key

    path('listar/campos/', CampoList.as_view(), name="listar-campos"),  # int pk = primari key
    path('listar/atividades/', AtividadeList.as_view(), name="listar-atividades"),  # int pk = primari key
    path('listar/status/', StatusList.as_view(), name="listar-status"),  # int pk = primari key
    path('listar/classes/', ClasseList.as_view(), name="listar-classes"),  # int pk = primari key
    path('listar/campus/', CampusList.as_view(), name="listar-campuss"),  # int pk = primari key

]