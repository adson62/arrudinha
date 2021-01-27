from django.urls import path
from . import views

app_name = 'mensagens'
urlpatterns = [
	path('', views.index, name='index'),
	path('mensagens/', views.MsgListView.as_view(), name='mensagens'),
	path("mensagens/<int:pk>/", views.DetailView.as_view(), name='detail'),
	path("mensagens/cadastrar/", views.cadastrarMensagens, name='cadastrarMensagens'),
	path("mensagens/<int:id>/editar/", views.editarMensagens, name='editarMensagens'),
	path("mensagens/<int:id>/excluir/", views.excluirMensagensBotao, name='excluirMensagensBotao'),
	path("mensagens/<int:id>/excluir/confirm", views.excluirMensagens, name='excluirMensagens'),
]